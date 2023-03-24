# coding:utf-8
import math

import pandas as pd
import datetime

from vehicledataanalysisinterfaceapi.utils.getWeatherConditions import getWeatherConditionByCoordinateAndDate


def trafficAllStatistics(df):
    return




# 计算一个司机多天内疲劳驾驶的总时长和次数
def fatigueDriving(df):
    """
    计算一个司机多天内疲劳驾驶的总时长和次数
    :param df: 传入的数据
    :return:
    """
    rows = df.shape[0]
    sumDriveTime = 0  # 一辆车的总疲劳驾驶累计时长
    sumDriveCount = 0  # 疲劳驾驶累计次数
    fatigueDriveCount = 0  # 当天疲劳驾驶累计次数
    fatigueDriveTime = 0  # 当天疲劳驾驶累计时长
    item = df.iloc[0]
    day = datetime.datetime.strptime(df.loc[0]['location_time'], '%Y-%m-%d %H:%M:%S').day  # 当前日期

    drive = False
    setOffTime = datetime.datetime.strptime(df.loc[0]['location_time'], '%Y-%m-%d %H:%M:%S')
    startRestTime = 0  # 开始休息的时间

    rest = False
    for i in range(1, rows):
        item = df.iloc[i]
        curTime = datetime.datetime.strptime(df.loc[i]['location_time'], '%Y-%m-%d %H:%M:%S')
        lastTime = datetime.datetime.strptime(df.loc[i - 1]['location_time'], '%Y-%m-%d %H:%M:%S')
        timeInterval = (curTime - lastTime).total_seconds()
        # if curTime.day!=day:
        # 	print("new day")
        if curTime.day != day or (timeInterval > 1200 and drive) or i == (rows - 1):
            # 日期变化或者出现相邻两条数据之间时间间隔大于20分钟，需要结束前面的统计
            day = curTime.day

            if (lastTime - setOffTime).total_seconds() > 14400:
                # print('4 hours')
                fatigueDriveCount += 1
                sumDriveTime += (lastTime - setOffTime).total_seconds()
            if fatigueDriveCount <= 1 and fatigueDriveTime > 28800:
                # 单次连续驾驶行为小于4并且当日驾驶时长大于8小时，则fatigueDriveCount加1
                fatigueDriveCount += 1
                # print('addition')
                if fatigueDriveCount == 1:
                    # 若原来的单次连续驾驶行为是0，当日驾驶时长超过8小时，则表明都是不连续的小的分散时间段，将fatigueDriveTime加入总的驾驶时长
                    sumDriveTime += fatigueDriveTime
                # print('8 hours')
            sumDriveCount += fatigueDriveCount
            fatigueDriveCount = 0
            fatigueDriveTime = 0
            drive = False
        # 开始单次连续驾驶行为
        if item[8] != 0 and not drive:
            drive = True
            setOffTime = curTime
        elif item[8] == 0 and drive and not rest:
            startRestTime = curTime
            rest = True
        elif item[8] != 0 and drive and rest:
            restTime = lastTime - startRestTime
            rest = False
            if restTime.total_seconds() >= 1200:  # 休息够20分钟，开车状态变为false,重新记录单次连续驾驶行为
                delta = startRestTime - setOffTime
                # 结束当次连续驾驶
                drive = False
                if delta.total_seconds() > 14400:  # 持续驾驶超过4小时
                    fatigueDriveCount += 1
                    # print('4 hours')
                    sumDriveTime += delta.total_seconds()
        elif item[8] != 0 and drive and not rest:
            fatigueDriveTime += timeInterval
    sumDriveTimeInHours = round(sumDriveTime, 2)  # 保留两位数
    return [sumDriveTimeInHours, sumDriveCount]


# 统计单次运行线路汽车的怠速预热累计时长和次数
def idle_preheatint(df):
    """
    统计单次运行线路汽车的怠速预热累计时长和次数
    :param df:  传入的数据
    :return:
    """
    rows = df.shape[0]
    CurDayFirstFrame = True  # 当日首次点火
    day = datetime.datetime.now().day
    startIdlePreheatTime = 0
    timeSum = 0
    count = 0
    isIdle = False
    for i in range(0, rows):
        item = df.iloc[i]
        # 新的一天
        if day != datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S').day:
            CurDayFirstFrame = True
            day = datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S').day
        if item['acc_state'] == 1 and item['gps_speed'] == 0:
            # 发生车辆怠速行为
            if CurDayFirstFrame or df.iloc[i - 1]['acc_state'] == 0 or not isIdle:
                startIdlePreheatTime = datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S')
                CurDayFirstFrame = False
                isIdle = True
            if i == rows - 1:
                endIdlePreheatTime = datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S')
                timeInterval = (endIdlePreheatTime - startIdlePreheatTime).total_seconds()
                if timeInterval > 60:
                    timeSum += timeInterval
                    count += 1

        else:
            if isIdle:
                endIdlePreheatTime = datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S')
                timeInterval = (endIdlePreheatTime - startIdlePreheatTime).total_seconds()
                if timeInterval > 60:
                    timeSum += timeInterval
                    count += 1
                isIdle = False
    timeSum /= 60
    timeSum = round(timeSum, 2)
    return [count, timeSum]


# 统计单次运行线路汽车的超长怠速累计时长和次数
def idling(df):
    """
    统计单次运行线路汽车的超长怠速累计时长和次数
    :param df: 传入的数据
    :return:
    """
    rows = df.shape[0]
    timeSum = 0
    idlingCount = 0
    startIdlingTime = df.iloc[0]['location_time']

    isIdling = False
    for i in range(0, rows):
        item = df.iloc[i]
        acc = item['acc_state']
        speed = item['gps_speed']
        if acc == 1 and speed == 0:
            if isIdling:
                if i == rows - 1:
                    # 到达最后一行
                    endIdligTime = datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S')
                    timeInterval = (endIdligTime - startIdlingTime).total_seconds()
                    if timeInterval >= 60:
                        # 持续怠速超过60s，计数并累计时长
                        timeSum += timeInterval
                        idlingCount += 1
                    isIdling = False

            else:
                # 重新开始新的判断
                startIdlingTime = datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S')
                isIdling = True
                continue
        else:
            # 怠速行为结束
            if isIdling:
                endIdligTime = datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S')
                timeInterval = (endIdligTime - startIdlingTime).total_seconds()
                if timeInterval >= 60:
                    # 持续怠速超过60s，计数并累计时长
                    timeSum += timeInterval
                    idlingCount += 1
                isIdling = False

    return [timeSum, idlingCount]


# 求出一段路的急加速急减速次数和对应的时间
def acce_decelerate(df):
    """
    求出一段路的急加速急减速次数和对应的时间
    :param df: 传入的行车数据
    :return:
    """
    rows = df.shape[0]
    acc_count = dec_count = 0
    acc_time = list()
    dec_time = list()
    currentState = False  # false表示当前时间正在减速
    isAccelerate = [0]  # 记录每个时间点是不是加速或减速
    isDecelerate = [0]  # 第一个时刻不算加减速

    sumTime = 0  # 保存一段加速/减速的累计时间
    for i in range(0, rows - 1):
        lastItem = df.iloc[i]
        currentItem = df.iloc[i + 1]
        # 取出前后相邻的时间，计算差值
        lastTime = datetime.datetime.strptime(lastItem[7], '%Y-%m-%d %H:%M:%S')
        currentTime = datetime.datetime.strptime(currentItem[7], '%Y-%m-%d %H:%M:%S')
        delta = currentTime - lastTime
        # 时间间隔小于等于3s，考虑加减速
        timeInterval = delta.total_seconds()
        if timeInterval <= 3 and timeInterval != 0:
            lastSpeed = lastItem[8]
            currentSpeed = currentItem[8]

            a = (currentSpeed - lastSpeed) / (3.6 * timeInterval)  # 计算加速度

            if a < -3 and not currentState:  # 减速阶段，累加时间到sumTime
                sumTime += timeInterval
                isDecelerate.append(1)
                isAccelerate.append(0)
            elif a < -3 and currentState:  # 从加速进入减速
                acc_count += 1
                acc_time.append(sumTime)
                sumTime = timeInterval
                isAccelerate.append(0)
                isDecelerate.append(1)
                currentState = False
            elif a > 3 and currentState:  # 加速阶段
                sumTime += timeInterval
                isAccelerate.append(1)
                isDecelerate.append(0)
            elif a > 3 and not currentState:  # 从减速进入加速
                if (sumTime != 0):
                    dec_count += 1
                    dec_time.append(sumTime)
                sumTime = timeInterval
                currentState = True

        else:
            # 时间间隔不小于3s,不是连续的急加速急减速
            if not currentState:
                if (sumTime != 0):
                    dec_count += 1
                    dec_time.append(sumTime)
                    sumTime = 0
            else:
                acc_count += 1
                acc_time.append(sumTime)
                sumTime = 0
    return [acc_count, sum(acc_time), dec_count, sum(dec_time)]


# 计算单次路程的熄火滑行次数和时长
def SlideOnFrameOut(df):
    """
    计算单次路程的熄火滑行次数和时长
    :param df: 传入的行车数据
    :return:
    """
    rows = df.shape[0]
    isSlide = False
    startTime = 0
    sumTime = 0
    slideCount = 0
    startlng = 0
    startlat = 0

    for i in range(0, rows):
        item = df.iloc[i]

        acc_state = item[6]
        gps_speed = item[8]

        if acc_state == 0 and gps_speed < 50:
            if not isSlide:  # 开始熄火滑行
                isSlide = True
                startTime = datetime.datetime.strptime(item[7], '%Y-%m-%d %H:%M:%S')
                startlat = item[5]
                startlng = item[4]
            continue
        if isSlide:
            endTime = datetime.datetime.strptime(item[7], '%Y-%m-%d %H:%M:%S')
            timeInterval = (endTime - startTime).total_seconds()
            endlat = item[5]
            endlng = item[4]
            isSlide = False
            # 滑行时长大于等于3，并且经纬度有变化
            if timeInterval >= 3 and (startlng != endlng or startlat != endlat):
                sumTime += timeInterval
                slideCount += 1
    return [sumTime, slideCount]


# 超速判断，返回列表[超速时长，超速次数]
def overspeed(df, speed_max):
    """
    超速判断，返回列表
    :param df: 传入的数据
    :param speed_max:  最大速度
    :return:
    """
    Overspeed_Duration = 0  # 用来记录超速时长
    Overspeed_Frequency = 0  # 用来记录超速次数
    flag_list = [0 for i in range(df.__len__() + 3)]  # 初始化一个flag,用来标记当前记录是否已扫描
    for i in df.index:
        if df.loc[i]['gps_speed'] > speed_max and flag_list[i] == 0:
            t1 = i  # 超速开始时间
            n = i + 1
            while n < df.__len__() and df.loc[n]['gps_speed'] > speed_max:
                flag_list[n] = 1
                n += 1
            t2 = n - 1  # 超速结束时间
            time_len = pd.to_datetime(df.loc[t2]['location_time']) - pd.to_datetime(df.loc[t1]['location_time'])
            time_len = time_len.total_seconds()
            if time_len >= 3:  # 为防止gps漂移，超速时长至少为3秒才会被记录
                Overspeed_Duration += time_len
                Overspeed_Frequency += 1
    return (list([Overspeed_Duration, Overspeed_Frequency]))


# 统计单条道路急转弯次数
def suddenTurn(df, weatherDict):
    """
    统计单条道路急转弯次数
    :param df:  传入的数据
    :param weatherDict: 天气字典
    :return:
    """
    # 统计单条道路急转弯次数
    count = 0
    rows = df.shape[0]
    condition = getWeatherConditionByCoordinateAndDate(df, weatherDict)
    # print(condition)
    # 确定静摩擦系数
    mju = 0
    for weaTag in condition:
        if weaTag == '大暴雨' or weaTag == '暴雨' or weaTag == '大雨' or weaTag == "雨夹雪":
            mju = 0.3
            break
        elif '雨' in weaTag or '雪' in weaTag:
            mju = 0.7
            continue
        else:
            # 没有雨雪的情况
            if mju == 0:
                mju = 1
    # print(mju)
    angular_threhold = math.pi / 4
    if '大暴雨' in condition or '暴雨' in condition or '大雨' in condition or '雷雨' in condition:
        angular_threhold = math.pi / 6
    elif '小雨' in condition or '小到中雨' in condition or '中雨' in condition or '小雪' in condition or '阵雨' in condition or '雷阵雨' in condition or '雨夹雪' in condition or '零散雷雨' in condition:
        angular_threhold = (35 * math.pi / 180)
    elif '阴' in condition or '多云' in condition:
        angular_threhold = (40 * math.pi / 180)
    elif '雾' in condition or '扬沙' in condition or '浮尘' in condition:
        angular_threhold = (25 * math.pi / 180)

    for i in range(1, rows):
        item = df.iloc[i]
        lastItem = df.iloc[i - 1]
        lastSpeed = lastItem['gps_speed']
        speed = item['gps_speed']

        if lastSpeed > 0 and speed > 0:
            # 只有两个车辆的速度都大于0时才进行急转弯判断
            lastTime = datetime.datetime.strptime(lastItem['location_time'], '%Y-%m-%d %H:%M:%S')
            currentTime = datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S')
            timeInterval = (currentTime - lastTime).total_seconds()
            if timeInterval == 0:
                continue

            turnAngle = abs(item['direction_angle'] - lastItem['direction_angle'])
            # 转弯角度不超过180
            if turnAngle > 180:
                turnAngle = 360 - turnAngle
            avgSpeed = (lastSpeed + speed) / 7.2  # 取平均值并转换单位为米每秒
            angular_velocity = (turnAngle * math.pi / 180) / timeInterval  # 角速度
            # print(avgSpeed)
            # print(angular_velocity)
            # print("\n")
            if angular_velocity > 0:
                # 转弯角度不为零才计算转弯半径
                radius = round((avgSpeed / angular_velocity), 2)
                # print(radius)
                # print("\n")
                # 根据静摩擦力提供向心力计算速度阈值，大于此速度为可能打滑
                speedThreshold = math.sqrt(mju * 9.8 * radius)
                # print(speedThreshold)
                # print(avgSpeed)

                if avgSpeed > speedThreshold:
                    count += 1
                    continue
                else:
                    if angular_velocity > angular_threhold:
                        # 转弯角速度过大
                        count += 1
    # print(count)
    return count