# coding:utf-8
import math

import pandas as pd
import time
import datetime
import numpy as np


def composetime(time1):
    """
    时间转换方法 将"%Y-%m-%d %H:%M:%S" 格式的数据 转换成时间戳
    :param time1: 需要转换的数据
    :return: time4 转换后的时间戳
    """
    time2 = datetime.datetime.strptime(time1, "%Y-%m-%d %H:%M:%S")
    time3 = time.mktime(time2.timetuple())
    time4 = int(time3)
    return time4


def zeroVelocityProcessing(drivingdata):
    """
    # 元组（start_i, end_i, num）格式
    :param drivingdata:  传入车辆行驶数据
    :return: data2 返回预处理后的数据 转换为dataframe格式
    """
    # 删除无用特征列
    data = drivingdata.drop(['right_turn_signals', 'left_turn_signals', 'hand_brake', 'foot_brake'], axis=1)

    idx_list = []  # 索引区间
    start_idx = None  # 起始索引
    end_idx = None  # 终止索引
    num = 1  # 区间内记录数
    move_onetime = 0
    move_alltime = 1
    zerovelocityinterval = []  # 零速度区间
    arr = data.to_numpy()  # 转换成np 进行遍历

    # 取出速度为 0 的行
    zero_speed_df = data[data['gps_speed'] == 0]

    # 获取连续区间的开始和结束索引值
    for i, row in zero_speed_df.iterrows():
        if start_idx is None:
            start_idx = i
        elif i != end_idx + 1:
            idx_list.append((start_idx, end_idx, end_idx - start_idx + 1))
            start_idx = i
        end_idx = i
    if start_idx is not None:
        idx_list.append((start_idx, end_idx, end_idx - start_idx + 1))

    newzerovelocityinterval = idx_list.copy()  # 新零速度区间
    # 零速度区间再划分 加速区间 减速区间  点火状态的改变
    for i in zerovelocityinterval:
        for num in range(i[0], i[1] + 1):
            if (arr[num][5] == 0):
                index = zerovelocityinterval.index(i)
                newzerovelocityinterval.pop(index)  # 移除原有零速度区间
                newzerovelocityinterval.insert(index, (i[0], num - 1, num - i[0]))  # 减速区间
                num2 = num
                # 找到加速区间起点
                while (num2 < len(arr) and arr[num2][5] == 0):
                    num2 += 1
                    pass
                newzerovelocityinterval.append((num2, i[1], i[1] + 1 - num2))  # 加速区间
                break
                pass
            pass
        pass

    # 将新的零速度区间进行排序
    newzerovelocityinterval.sort()

    """
    表示在该零速度区间车辆始终未移动 move_onetime=0
    表示在该零速度区间车辆发生过移动 move_onetime=1
    表示在该零速度区间车辆存在静止的情况 move_alltime=0
    表示在该零速度区间车辆始终在移动move_alltime=1
    带标识元组（start_i, end_i, num,move_onetime ,move_alltime ）格式
    """
    tagzerovelocityinterval = []  # 带标识的零速度区间
    for i in newzerovelocityinterval:
        accstateone = 0
        accstatezero = 0
        for num in range(i[0], i[1] + 1):
            if (arr[num][5] == 1):
                accstateone += 1
            elif (arr[num][5] == 0):
                accstatezero += 1
            pass
        if (accstateone == i[2]):
            tagzerovelocityinterval.append((i[0], i[1], i[2], 1, 1))  # 始终在移动
            pass
        elif (accstatezero == i[2]):
            tagzerovelocityinterval.append((i[0], i[1], i[2], 0, 0))  # 始终未移动
            pass
        else:
            tagzerovelocityinterval.append((i[0], i[1], i[2], 1, 0))  # 存在移动和静止情况
            pass
        pass

    """
        将数据转换后根据速度公式计算出加速度
    """
    t = []
    v = []
    for i in range(len(data["location_time"])):
        if (len(data["location_time"]) != i + 1):
            t1 = composetime(data["location_time"][i])
            t2 = composetime(data["location_time"][i + 1])
            v1 = data["gps_speed"][i]
            v2 = data["gps_speed"][i + 1]
            t0 = t2 - t1
            v0 = v2 - v1
            t.append(t0)
            v.append(v0)

    # 根据不同的情况对零速度进行填充
    limitspeed = 10
    for i in range(len(arr)):
        for j in tagzerovelocityinterval:
            if (i == j[0]):
                # 1如果区间长度小于等于 5，且区间两侧速度都不为 0，则视作传感器短暂失灵，使用区间两端非 0 速度的平均值填充，
                if (j[2] <= 5 and arr[j[0] - 1][7] > 0 and arr[j[1] + 1][7] > 0):
                    avgspeed = (arr[j[0] - 1][7] + arr[j[1] + 1][7]) / 2
                    for num in range(j[0], j[1] + 1):
                        arr[num][7] = avgspeed
                        pass
                    continue
                    pass
                # 2如果move_onetime = 0，说明车辆没有发生移动，如果区间两端非0速度小于阈值 limitspeed 则保持速度为 0 不变
                # 7如果区间两端非 0 速度大于阈值 表示车辆在高速行驶状态下突然转为静止发生的原因可能是车辆在高速行驶状态时，速度记录传感器失灵 使用区间两端非 0 速度的平均值填充
                elif (j[3] == 0 and arr[j[0] - 1][7] > limitspeed and arr[j[1] + 1][7] > limitspeed):
                    avgspeed = (arr[j[0] - 1][7] + arr[j[1] + 1][7]) / 2
                    for num in range(j[0], j[1] + 1):
                        arr[num][7] = avgspeed
                        pass
                    continue
                    pass
                # 3如果 move_alltime = 1，说明车辆始终在移动，但是没有被记录仪记录，很可能是在发生 10km/h 以下的低速移动，例如堵车等此时用区间两端的非 0 速度的平均值填充
                elif (j[4] == 1):
                    avgspeed = (arr[j[0] - 1][7] + arr[j[1] + 1][7]) / 2
                    for num in range(j[0], j[1] + 1):
                        arr[num][7] = avgspeed
                        pass
                    continue
                    pass
                # 4如果 move_alltime = 0，说明车辆发生过移动，但没有始终在移动，此时应当对区间 两端的速度进行匀加速匀减速填充
                # 如果记录小于十条直接 用十条的前后的平均速度填充
                elif (j[4] == 0 and j[2] <= 10):
                    if (arr[j[0] - 1][7] == 0 and arr[j[1] + 1][7] != 0):
                        avgspeed = (arr[j[0] - 1][7] + arr[j[1] + 1][7]) / 2
                        for num in range(j[0], j[1] + 1):
                            arr[num][7] = avgspeed
                            pass
                        continue
                    pass
                elif (j[4] == 0 and j[2] > 10):
                    # 分成十个不同加速度段
                    speeds = math.ceil(j[2] / 10)
                    # 匀加速
                    if (arr[j[0] - 1][7] == 0 and arr[j[1] + 1][7] != 0):
                        # 取整加速度
                        acceleratedspeed = math.ceil(arr[j[1] + 1][7] / 10)
                        # 分别给每个加速度段设置
                        count = 1
                        for num in range(j[0], j[1] + 1):
                            if (count % speeds == 0):
                                acceleratedspeed += 1
                            arr[num][7] = acceleratedspeed
                            count += 1
                            pass
                    else:
                        # 取整加速度
                        acceleratedspeed = math.ceil(arr[j[0] - 1][7] / 10)
                        # 分别给每个加速度段设置
                        count = 1
                        for num in range(j[0], j[1] + 1):
                            if (count % speeds == 0):
                                acceleratedspeed -= 1
                            arr[num][7] = acceleratedspeed
                            count += 1
                            pass
                    continue
                    pass
    data2 = pd.DataFrame(arr, columns=data.columns)  # 处理完将数据转回DataFrame
    return data2


# def zeroVelocityProcessing(drivingdata):
#     # 删除无用特征列
#     df = drivingdata.drop(['right_turn_signals', 'left_turn_signals', 'hand_brake', 'foot_brake'], axis=1)
#
#     # 取出速度为 0 的行
#     zero_speed_df = df[df['gps_speed'] == 0]
#
#     # 获取连续区间的开始和结束索引值
#     idx_list = []
#     start_idx = None
#     end_idx = None
#     for i, row in zero_speed_df.iterrows():
#         if start_idx is None:
#             start_idx = i
#         elif i != end_idx + 1:
#             idx_list.append((start_idx, end_idx, end_idx - start_idx + 1))
#             start_idx = i
#         end_idx = i
#     if start_idx is not None:
#         idx_list.append((start_idx, end_idx, end_idx - start_idx + 1))

