import pandas as pd
import numpy as np
import datetime
import os
import json
import urllib.request
import sys
import copy
import math

from vehicledataanalysisinterfaceapi.utils.TrafficConditionAnalysis import SlideOnFrameOut, acce_decelerate, overspeed, \
    fatigueDriving, suddenTurn, idle_preheatint, idling
from vehicledataanalysisinterfaceapi.utils.getWeatherConditions import genLocation_Date_Weather_Dict, \
    getWeatherConditionByCoordinateAndDate


def add_bias(mtx, bias_mtx):
    for i in range(mtx.shape[0]):
        for j in range(mtx.shape[0]):
            if i < j:  # 对于矩阵的右上三角
                v = mtx[i, j]
                B = bias_mtx[i, j]
                if v >= 1:
                    if v + B >= 1:
                        v2 = v + B
                    elif v + B < 1:
                        v2 = 1 / (2 - (v + B))
                elif v < 1:
                    if (1 / v) - B >= 1:
                        v2 = 1 / ((1 / v) - B)
                    elif (1 / v) - B < 1:
                        v2 = 2 + B - (1 / v)
                mtx[i, j] = v2
            elif i > j:  # 对于矩阵的左下三角
                mtx[i, j] = 1 / mtx[j, i]
    return mtx


bias_light_rain = np.matrix(
    [0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_moderate_rain = np.matrix(
    [0, 0, 0, 1.5, 1.5, 0, 0,
     0, 0, 0, 1.5, 1.5, 0, 0,
     0, 0, 0, 1.5, 1.5, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_heavy_rain = np.matrix(
    [0, 0, 0, 2, 2, 0, 0,
     0, 0, 0, 2, 2, 0, 0,
     0, 0, 0, 2, 2, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_rainstorm = np.matrix(
    [0, 0, 0, 2.5, 2.5, 0, 0,
     0, 0, 0, 2.5, 2.5, 0, 0,
     0, 0, 0, 2.5, 2.5, 0, 0,
     0, 0, 0, 0, 1, 0, 0,
     0, 0, 0, 0, 0, -1, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_light_snow = np.matrix(
    [0, 0, 0, 1.5, 1.5, 0, 0,
     0, 0, 0, 1.5, 1.5, 0, 0,
     0, 0, 0, 1.5, 1.5, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_sunny = np.matrix(
    [0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_overcast = np.matrix(
    [0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_clody = np.matrix(
    [0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_shower = np.matrix(
    [0, 0, 0, 0.5, 0.5, 0, 0,
     0, 0, 0, 0.5, 0.5, 0, 0,
     0, 0, 0, 0.5, 0.5, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_thunder_shower = np.matrix(
    [0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_fog = np.matrix(
    [0, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_sleet = np.matrix(
    [0, 0, 0, 1.5, 1.5, 0, 0,
     0, 0, 0, 1.5, 1.5, 0, 0,
     0, 0, 0, 1.5, 1.5, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_floating_dust = np.matrix(
    [0, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_blowing_sand = np.matrix(
    [0, 1, 1, 1, 1, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, ]).reshape(7, 7)
bias_EC_light_rain = np.matrix(
    [0, 1, 1, 1, 1, 0,
     0, 0, 0, 0, 0, -1,
     0, 0, 0, 0, 0, -1,
     0, 0, 0, 0, 0, -1,
     0, 0, 0, 0, 0, -1,
     0, 0, 0, 0, 0, 0, ]).reshape(6, 6)
bias_EC_heavy_rain = np.matrix(
    [0, 2, 2, 2, 2, 0,
     0, 0, 0, 0, 0, -2,
     0, 0, 0, 0, 0, -2,
     0, 0, 0, 0, 0, -2,
     0, 0, 0, 0, 0, -2,
     0, 0, 0, 0, 0, 0, ]).reshape(6, 6)
bias_EC_sunny = np.matrix(
    [0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, ]).reshape(6, 6)


# 根据天气情况确定bias矩阵，输入天气列表（包含1~3个str元素），返回bias和bias_EC矩阵：
def bias_determine(weather):
    if len(weather) >= 1:
        if weather[0] in ['小雨', '小到中雨']:
            bias1 = bias_light_rain
            bias1_EC = bias_EC_light_rain
        if weather[0] == '中雨':
            bias1 = bias_moderate_rain
            bias1_EC = bias_EC_light_rain
        if weather[0] == '大雨':
            bias1 = bias_heavy_rain
            bias1_EC = bias_EC_heavy_rain
        if weather[0] in ['暴雨', '大暴雨', '雷雨']:
            bias1 = bias_rainstorm
            bias1_EC = bias_EC_heavy_rain
        if weather[0] == '小雪':
            bias1 = bias_light_snow
            bias1_EC = bias_EC_light_rain
        if weather[0] in ['晴', '未知']:
            bias1 = bias_sunny
            bias1_EC = bias_EC_sunny
        if weather[0] == '阴':
            bias1 = bias_overcast
            bias1_EC = bias_EC_sunny
        if weather[0] == '多云':
            bias1 = bias_clody
            bias1_EC = bias_EC_sunny
        if weather[0] == '阵雨':
            bias1 = bias_shower
            bias1_EC = bias_EC_light_rain
        if weather[0] in ['雷阵雨', '零散雷雨']:
            bias1 = bias_thunder_shower
            bias1_EC = bias_EC_light_rain
        if weather[0] == '雾':
            bias1 = bias_fog
            bias1_EC = bias_EC_sunny
        if weather[0] == '雨夹雪':
            bias1 = bias_sleet
            bias1_EC = bias_EC_light_rain
        if weather[0] == '浮尘':
            bias1 = bias_floating_dust
            bias1_EC = bias_EC_sunny
        if weather[0] == '扬沙':
            bias1 = bias_blowing_sand
            bias1_EC = bias_EC_sunny
        if len(weather) >= 2:
            if weather[1] in ['小雨', '小到中雨']:
                bias2 = bias_light_rain
                bias2_EC = bias_EC_light_rain
            if weather[1] == '中雨':
                bias2 = bias_moderate_rain
                bias2_EC = bias_EC_light_rain
            if weather[1] == '大雨':
                bias2 = bias_heavy_rain
                bias2_EC = bias_EC_heavy_rain
            if weather[1] in ['暴雨', '大暴雨', '雷雨']:
                bias2 = bias_rainstorm
                bias2_EC = bias_EC_heavy_rain
            if weather[1] == '小雪':
                bias2 = bias_light_snow
                bias2_EC = bias_EC_light_rain
            if weather[1] == '晴':
                bias2 = bias_sunny
                bias2_EC = bias_EC_sunny
            if weather[1] == '阴':
                bias2 = bias_overcast
                bias2_EC = bias_EC_sunny
            if weather[1] == '多云':
                bias2 = bias_clody
                bias2_EC = bias_EC_sunny
            if weather[1] == '阵雨':
                bias2 = bias_shower
                bias2_EC = bias_EC_light_rain
            if weather[1] in ['雷阵雨', '零散雷雨']:
                bias2 = bias_thunder_shower
                bias2_EC = bias_EC_light_rain
            if weather[1] == '雾':
                bias2 = bias_fog
                bias2_EC = bias_EC_sunny
            if weather[1] == '雨夹雪':
                bias2 = bias_sleet
                bias2_EC = bias_EC_light_rain
            if weather[1] == '浮尘':
                bias2 = bias_floating_dust
                bias2_EC = bias_EC_sunny
            if weather[1] == '扬沙':
                bias2 = bias_blowing_sand
                bias2_EC = bias_EC_sunny
            if len(weather) == 3:
                if weather[2] in ['小雨', '小到中雨']:
                    bias3 = bias_light_rain
                    bias3_EC = bias_EC_light_rain
                if weather[2] == '中雨':
                    bias3 = bias_moderate_rain
                    bias3_EC = bias_EC_light_rain
                if weather[2] == '大雨':
                    bias3 = bias_heavy_rain
                    bias3_EC = bias_EC_heavy_rain
                if weather[2] in ['暴雨', '大暴雨', '雷雨']:
                    bias3 = bias_rainstorm
                    bias3_EC = bias_EC_heavy_rain
                if weather[2] == '小雪':
                    bias3 = bias_light_snow
                    bias3_EC = bias_EC_light_rain
                if weather[2] == '晴':
                    bias3 = bias_sunny
                    bias3_EC = bias_EC_sunny
                if weather[2] == '阴':
                    bias3 = bias_overcast
                    bias3_EC = bias_EC_sunny
                if weather[2] == '多云':
                    bias3 = bias_clody
                    bias3_EC = bias_EC_sunny
                if weather[2] == '阵雨':
                    bias3 = bias_shower
                    bias3_EC = bias_EC_light_rain
                if weather[2] in ['雷阵雨', '零散雷雨']:
                    bias3 = bias_thunder_shower
                    bias3_EC = bias_EC_light_rain
                if weather[2] == '雾':
                    bias3 = bias_fog
                    bias3_EC = bias_EC_sunny
                if weather[2] == '雨夹雪':
                    bias3 = bias_sleet
                    bias3_EC = bias_EC_light_rain
                if weather[2] == '浮尘':
                    bias3 = bias_floating_dust
                    bias3_EC = bias_EC_sunny
                if weather[2] == '扬沙':
                    bias3 = bias_blowing_sand
                    bias3_EC = bias_EC_sunny
    if len(weather) == 1:
        bias = bias1
        bias_EC = bias1_EC
    if len(weather) == 2:
        bias = (bias1 + bias2) / 2
        bias_EC = (bias1_EC + bias2_EC) / 2
    if len(weather) == 3:
        bias = (bias1 + bias2 + bias3) / 3
        bias_EC = (bias1_EC + bias2_EC + bias3_EC) / 3
    return [bias, bias_EC]


# 一致性检验,输入判断矩阵，输出CR值：
def Consistency_test(mtx):
    n = mtx.shape[0]
    a, b = np.linalg.eig(mtx)
    max_chrct_value = max(a)  # 求判断矩阵的最大特征值
    max_chrct_value = max_chrct_value.real
    CI = (max_chrct_value - n) / (n - 1)
    RI = np.array([0, 0, 0, 0.52, 0.89, 1.12, 1.24, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58])
    CR = CI / RI[n]
    return round(CR, 3)


# 列向量归一化：
def normalization(mtx):  # 比例归一化
    for i in range(mtx.shape[1]):  # 对矩阵的每一列进行循环
        sum = mtx[:, i].sum()  # 当前列的和
        for j in range(mtx.shape[0]):  # 对每一列的每个元素进行循环
            mtx[j, i] = mtx[j, i] / sum
    return mtx


# 车速稳定性判断，返回车速标准差：
def Speed_Stability(df):
    return np.std(df['gps_speed'], ddof=1)


# 统计危险驾驶行为
def Static_Behavior(df):
    """
    统计危险驾驶行为
    :param df: 导入的驾驶数据
    :return:speed_std 车速方差, rapid_acc_numbers 急加速次数, rapid_acc_duration 急加速时长, rapid_dec_numbers 急减速次数, rapid_dec_duration 急减速时长,
            slide_frameOut_duration 熄火滑行时长, slide_frameOut_numbers 熄火滑行次数, overspeed_numbers 超速次数, overspeed_duration 超速时长,
            fatigueDriving_numbers 疲劳驾驶次数, fatigueDriving_hours 疲劳驾驶时长, suddenTurn_numbers 急转弯次数, idle_preheating_numbers 怠速预热次数,
            idle_preheating_mins 怠速预热时长, overlong_idle_numbers 超长怠速次数, overlong_idle_mins 超长怠速时长
    """
    weather_dict = genLocation_Date_Weather_Dict() # 获取天气字典
    speed_std = Speed_Stability(df)  # 车速方差
    acc_dec = acce_decelerate(df)  # 急加速急减速输出列表
    rapid_acc_numbers = acc_dec[0]  # 急加速次数
    rapid_acc_duration = int(acc_dec[1])  # 急加速时长
    rapid_dec_numbers = acc_dec[2]  # 急减速次数
    rapid_dec_duration = int(acc_dec[3])  # 急减速时长
    slide_frameOut_list = SlideOnFrameOut(df)  # 熄火滑行输出列表
    slide_frameOut_duration = slide_frameOut_list[0]  # 熄火滑行时长
    slide_frameOut_numbers = slide_frameOut_list[1]  # 熄火滑行次数
    overspeed_list = overspeed(df, 100)  # 超速输出列表
    overspeed_numbers = overspeed_list[1]  # 超速次数
    overspeed_duration = overspeed_list[0]  # 超速时长
    fatigueDriving_list = fatigueDriving(df)  # 疲劳驾驶输出列表
    fatigueDriving_numbers = fatigueDriving_list[1]  # 疲劳驾驶次数
    fatigueDriving_hours = fatigueDriving_list[0]  # 疲劳驾驶时长
    suddenTurn_numbers = suddenTurn(df, weather_dict)  # 急转弯次数
    idle_preheating_list = idle_preheatint(df)  # 怠速预热输出列表
    idle_preheating_numbers = idle_preheating_list[0]  # 怠速预热次数
    idle_preheating_mins = idle_preheating_list[1]  # 怠速预热时长
    overlong_idle_list = idling(df)  # 超长怠速输出列表
    overlong_idle_numbers = overlong_idle_list[0]  # 超长怠速次数
    overlong_idle_mins = overlong_idle_list[1]  # 超长怠速时长

    return [speed_std, rapid_acc_numbers, rapid_acc_duration, rapid_dec_numbers, rapid_dec_duration,
            slide_frameOut_duration, slide_frameOut_numbers, overspeed_numbers, overspeed_duration,
            fatigueDriving_numbers, fatigueDriving_hours, suddenTurn_numbers, idle_preheating_numbers,
            idle_preheating_mins, overlong_idle_numbers, overlong_idle_mins]


# 驾驶行为评分
def DrivingBehaviorScore(df):
    """
    驾驶行为评分
    :param df: 传进来的数据
    :return:
    """
    mtx_EC = np.matrix([1, 1 / 2, 1 / 3, 1 / 2, 1 / 2, 1 / 3,
                        2, 1, 1 / 2, 1, 1, 1 / 2,
                        3, 2, 1, 2, 2, 1,
                        2, 1, 1 / 2, 1, 1, 1 / 2,
                        2, 1, 1 / 2, 1, 1, 1 / 2,
                        3, 2, 1, 2, 2, 1, ]).reshape(6, 6)  # 节能（Energy Conservation）判断矩阵
    mtx = np.matrix([1, 4, 2, 3, 3, 1, 3,
                     1 / 4, 1, 1 / 2, 1 / 2, 1 / 2, 1 / 3, 2,
                     1 / 2, 2, 1, 2, 2, 1 / 2, 2,
                     1 / 2, 2, 1 / 2, 1, 1, 1 / 2, 2,
                     1 / 3, 2, 1 / 2, 1, 1, 1 / 2, 1 / 2,
                     1, 3, 2, 2, 2, 1, 3,
                     1 / 3, 1 / 2, 1 / 2, 1 / 2, 2, 1 / 3, 1]).reshape(7, 7)  # 安全判断矩阵
    mtx_backup = copy.deepcopy(mtx)  # 备份一下原始矩阵，以便原始矩阵被修改时可以恢复
    mtx_EC_backup = copy.deepcopy((mtx_EC))

    # 对判断矩阵进行调整：
    weather_dict = genLocation_Date_Weather_Dict()
    weather = list(getWeatherConditionByCoordinateAndDate(df, weather_dict))
    print("当前路段天气：", weather)
    bias = bias_determine(weather)

    mtx_adjust = add_bias(mtx, bias[0])
    mtx_EC_adjust = add_bias(mtx_EC, bias[1])

    # 用调整后的安全判断矩阵计算权重：
    CR = Consistency_test(mtx_adjust)  # 一致性检验
    print("调整后的安全模型判断矩阵一致性检验：CR=", CR)
    mtx_adjust = normalization(mtx_adjust)  # 列向量归一化
    weight = np.array([float(0) for i in range(mtx_adjust.shape[1])])  # 创建weight向量
    for j in range(mtx_adjust.shape[1]):
        weight[j] = mtx_adjust[j, :].mean()  # 得出权重列表
    print("安全指标权重列表：\n", weight)
    print("(超速，急加速，急减速，车速稳定性，熄火滑行，疲劳驾驶,急转弯)")

    # 用调整后的节能判断矩阵计算节能指标权重：
    CR_EC = Consistency_test(mtx_EC_adjust)
    print("调整后的节能模型判断矩阵一致性检验：CR=", CR_EC)
    mtx_EC_adjust = normalization(mtx_EC_adjust)  # 列向量归一化
    weight_EC = np.array([float(0) for i in range(mtx_EC_adjust.shape[1])])  # 创建weight向量
    for p in range(mtx_EC_adjust.shape[1]):
        weight_EC[p] = mtx_EC_adjust[p, :].mean()  # 得出权重列表
    print("节能指标权重列表：\n", weight_EC)
    print("(怠速预热，超速，急加速，急减速，车速稳定性，超长怠速)")

    speed_std = Speed_Stability(df)  # 车速方差
    acc_dec = acce_decelerate(df)  # 急加速急减速输出列表
    rapid_acc_numbers = acc_dec[0]  # 急加速次数
    rapid_acc_duration = int(acc_dec[1])  # 急加速时长
    rapid_dec_numbers = acc_dec[2]  # 急减速次数
    rapid_dec_duration = int(acc_dec[3])  # 急减速时长
    slide_frameOut_list = SlideOnFrameOut(df)  # 熄火滑行输出列表
    slide_frameOut_duration = slide_frameOut_list[0]  # 熄火滑行时长
    slide_frameOut_numbers = slide_frameOut_list[1]  # 熄火滑行次数
    overspeed_list = overspeed(df, 100)  # 超速输出列表
    overspeed_numbers = overspeed_list[1]  # 超速次数
    overspeed_duration = overspeed_list[0]  # 超速时长
    fatigueDriving_list = fatigueDriving(df)  # 疲劳驾驶输出列表
    fatigueDriving_numbers = fatigueDriving_list[1]  # 疲劳驾驶次数
    fatigueDriving_hours = fatigueDriving_list[0]  # 疲劳驾驶时长
    suddenTurn_numbers = suddenTurn(df, weather_dict)  # 急转弯次数
    idle_preheating_list = idle_preheatint(df)  # 怠速预热输出列表
    idle_preheating_numbers = idle_preheating_list[0]  # 怠速预热次数
    idle_preheating_mins = idle_preheating_list[1]  # 怠速预热时长
    overlong_idle_list = idling(df)  # 超长怠速输出列表
    overlong_idle_numbers = overlong_idle_list[0]  # 超长怠速次数
    overlong_idle_mins = overlong_idle_list[1]  # 超长怠速时长

    # 计算得分：
    # 车速稳定性得分score_stb：
    if speed_std <= 20:
        score_stb = 100
    elif 20 < speed_std <= 40:
        score_stb = 80
    elif speed_std > 40:
        score_stb = 60

    # 急加速次数得分：
    score_acc_numbers = 100 - 15 * rapid_acc_numbers
    if score_acc_numbers < 0: score_acc_numbers = 0
    # 急加速时长得分：
    score_acc_duration = 100 - 0.8 * int(rapid_acc_duration)
    if score_acc_duration < 0: score_acc_duration = 0
    # 急加速总得分:
    score_acc = (score_acc_numbers / 2) + (score_acc_duration / 2)
    # 急减速次数得分：
    score_dec_numbers = 100 - 15 * rapid_dec_numbers
    if score_dec_numbers < 0: score_dec_numbers = 0
    # 急减速时长得分：
    score_dec_duration = 100 - 0.8 * int(rapid_dec_duration)
    if score_dec_duration < 0: score_dec_duration = 0
    # 急减速总得分:
    score_dec = (score_dec_numbers / 2) + (score_dec_duration / 2)

    # 超速次数得分：
    score_overspeed_numbers = 100 - 15 * overspeed_numbers
    if score_overspeed_numbers < 0: score_overspeed_numbers = 0
    # 超速时长得分：
    score_overspeed_duration = 100 - overspeed_duration
    if score_overspeed_duration < 0: score_overspeed_duration = 0
    # 超速总得分:
    score_overspeed = (score_overspeed_duration / 2) + (score_overspeed_numbers / 2)

    # 熄火滑行次数得分：
    score_slide_numbers = 100 - 20 * slide_frameOut_numbers
    if score_slide_numbers < 0: score_slide_numbers = 0
    # 熄火滑行时长得分：
    if slide_frameOut_duration <= 1:
        score_slide_duration = 100
    elif slide_frameOut_duration > 1:
        score_slide_duration = 100 - 10 * slide_frameOut_duration
        if score_slide_duration < 0: score_slide_duration = 0
    # 熄火滑行总得分：
    score_slide = (score_slide_numbers / 2) + (score_slide_duration / 2)

    # 疲劳驾驶次数得分：
    score_fati_numbers = 100 - 15 * fatigueDriving_numbers
    if score_fati_numbers < 0: score_fati_numbers = 0
    # 疲劳驾驶时长得分:
    if fatigueDriving_hours > 8:
        score_fati_hours = 0
    else:
        score_fati_hours = 100
    # 疲劳驾驶总得分：
    score_fati = (score_fati_hours / 2) + (score_fati_numbers / 2)

    # 急转弯得分：
    score_suddenTurn = 100 - 10 * suddenTurn_numbers
    if score_suddenTurn < 0: score_suddenTurn = 0

    # 怠速预热次数得分：
    score_idlePre_numbers = 100 - 15 * idle_preheating_numbers
    if score_idlePre_numbers < 0: score_idlePre_numbers = 0
    # 怠速预热时长得分：
    score_idlePre_mins = 100 - 2.5 * idle_preheating_mins
    if score_idlePre_mins < 0: score_idlePre_mins = 0
    # 怠速预热总得分：
    score_idlePre = (score_idlePre_numbers / 2) + (score_idlePre_mins / 2)

    # 超长怠速次数得分：
    score_overIdle_numbers = 100 - 10 * overlong_idle_numbers
    if score_overIdle_numbers < 0: score_overIdle_numbers = 0
    # 超长怠速时长得分：
    score_overIdle_mins = 100 - 0.8 * overlong_idle_mins
    if score_overIdle_mins < 0: score_overIdle_mins = 0
    # 超长怠速总得分：
    score_overIdle = (score_overIdle_numbers / 2) + (score_overIdle_mins / 2)

    # 计算安全模型总得分：
    score = weight[0] * score_overspeed + weight[1] * score_acc + weight[2] * score_dec + weight[3] * score_stb + \
            weight[4] * score_slide + weight[5] * score_fati + weight[6] * score_suddenTurn
    print("安全模型得分：", score)
    # 计算节能模型总得分：
    score_EC = weight_EC[0] * score_idlePre + weight_EC[1] * score_overspeed + weight_EC[2] * score_acc + \
               weight_EC[3] * score_dec + weight_EC[4] * score_stb + weight_EC[5] * score_overIdle
    print("节能模型得分：", score_EC)
    # 计算综合模型得分：
    score_total = (score / 2) + (score_EC / 2)
    print("综合模型得分：", score_total)
    mtx = copy.deepcopy(mtx_backup)  # 恢复初始判断矩阵
    mtx_EC = copy.deepcopy(mtx_EC_backup)
