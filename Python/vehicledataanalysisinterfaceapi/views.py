# coding:utf-8
import json

import pandas as pd
from django.http import JsonResponse
import threading

from django.apps import apps
from vehicledataanalysisinterfaceapi.utils.DataPreProcessing import zeroVelocityProcessing2
from vehicledataanalysisinterfaceapi.utils.DrawMap import drawMap, baseDBSCANMapNoiseReduction, kalman_filter
from vehicledataanalysisinterfaceapi.utils.DrivingBehaviorScore import DrivingBehaviorScore, Static_Behavior, \
    total_distance_driving_time_average_speed
from vehicledataanalysisinterfaceapi.utils.response.responsejava import datapreProcessingcallback, \
    datastatisticscallback, drawmapcallback, datascorecallback

# Create your views here.

# 设置javaWeb基础路径
javaFrontUrl = apps.get_app_config('vehicledataanalysisinterfaceapi').javawebpath
# csv文件保存路径
csvSavePath = apps.get_app_config('vehicledataanalysisinterfaceapi').filesavepath

# 车辆驾驶数据的字段
vehicleDrivingDataFields = ['totalDistance', 'drivingTime', 'meanSpeed','speedStd', 'rapidAccNumbers', 'rapidAccDuration', 'rapidDecNumbers', 'rapidDecDuration',
                  'slideFrameoutDuration', 'slideFrameoutNumbers', 'overspeedNumbers', 'overspeedDuration',
                  'fatiguedrivingNumbers', 'fatiguedrivingHours', 'suddenturnNumbers', 'idlePreheatingNumbers',
                  'idlePreheatingMins', 'overlongIdleNumbers', 'overlongIdleMins']

# 车辆驾驶得分的字段
vehicleDrivingBehaviorScoreFileds=['securityModelScore', 'energySavingModelScore', 'compositeModelScore']


def datapreprocessingapi(request):
    """
    数据预处理接口
    获取request 传入的csv文件 进行数据预处理后存储到指定位置 并返回处理结果
    :param request:  post请求
    :return: 返回Json数据
    """
    res = json.loads(request.body)
    filepath = javaFrontUrl + res["dataPath"]
    df = pd.read_csv(filepath)

    savepath = csvSavePath + res["dataPath"][len('/profile'):]

    # 在新线程中执行耗时操作 处理数据
    def process_data():
        df2 = zeroVelocityProcessing2(df)
        df2.to_csv(savepath)
        res["preprocessingState"] = 2
        datapreProcessingcallback(res)

    # 创建并启动新线程
    thread = threading.Thread(target=process_data)
    thread.start()

    request_data = {"code": 200, "message": "请求成功"}
    return JsonResponse(request_data, status=200, charset="utf-8")


def drawmapapi(request):
    """
    根据传入的行车数据绘制出行车路线图  内部进行数据的降噪处理
    :param request:  post请求
    :return: 返回Json数据
    """
    res = json.loads(request.body)
    filepath = javaFrontUrl + res["mapPath"]
    df = pd.read_csv(filepath)
    # 在新线程中执行耗时操作 处理数据
    def draw_map():
        df2 = baseDBSCANMapNoiseReduction(df)  # DBSCAN降噪
        df2 = kalman_filter(df2, 2.0)  # 基于卡尔曼滤波进行平滑曲线
        # df2 = correctionOfTrajectoryBaiDu(df2)  # 调用百度接口进行绑路
        res["buildMapStatus"] = 2
        res["mapPath"] = drawMap(df2)
        drawmapcallback(res)

    # 创建并启动新线程
    thread = threading.Thread(target=draw_map)
    thread.start()

    request_data = {"code": 200, "message": "请求成功"}
    return JsonResponse(request_data, status=200, charset="utf-8")


def trafficStatisticsapi(request):
    """
    根据传入的行车数据统计出当前车辆的数据
    获取request 传入的csv文件 统计出当前车辆的数据 并返回处理结果
    :param request:  post请求
    :return: 返回Json数据
    """
    res = json.loads(request.body)
    filepath = javaFrontUrl + res["dataPath"]
    df = pd.read_csv(filepath)

    # 在新线程中执行耗时操作 处理数据
    def statistics_data():
        drive_behavior_statics = Static_Behavior(df)
        # 给对应的字段进行数据填充
        count = 0
        for field in vehicleDrivingDataFields:
            res[field] = drive_behavior_statics[count]
            count += 1
        # 修改统计状态
        res["statisticalState"] = 2
        datastatisticscallback(res)

    # 创建并启动新线程
    thread = threading.Thread(target=statistics_data)
    thread.start()

    request_data = {"code": 200, "message": "请求成功", }
    return JsonResponse(request_data, status=200, charset="utf-8")


def drivingbehaviorevaluationapi(request):
    """
    计算车辆驾驶行为得分情况
    获取request 传入的csv文件 统计出当前车辆的数据 并返回处理结果
    :param request: post请求
    :return: 返回Json数据
    """
    # 取出数据
    res = json.loads(request.body)
    vehicleDrivingBehaviorScoreJson = json.loads(res.get("vehicleDrivingBehaviorScoreJson"))
    vehicleDrivingDataJson = json.loads(res.get("vehicleDrivingDataJson"))

    # 读取df数据
    filepath = javaFrontUrl + vehicleDrivingDataJson["dataPath"]
    df = pd.read_csv(filepath)

    statistics_values = []
    for field in vehicleDrivingDataFields:
        statistics_values.append(vehicleDrivingDataJson.get(field))

    # 在新线程中执行耗时操作 处理数据
    def driving_score():
        drive_score = DrivingBehaviorScore(df, statistics_values)
        # 给对应的字段进行数据填充
        count = 0
        for field in vehicleDrivingBehaviorScoreFileds:
            vehicleDrivingBehaviorScoreJson[field] = drive_score[count]
            count += 1
        # 修改统计状态
        vehicleDrivingBehaviorScoreJson["scoringStatus"] = 2
        datascorecallback(vehicleDrivingBehaviorScoreJson)

    # 创建并启动新线程
    thread = threading.Thread(target=driving_score)
    thread.start()

    request_data = {"code": 200, "message": "请求成功", }
    return JsonResponse(request_data, status=200, charset="utf-8")
