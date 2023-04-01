# coding:utf-8
import json

import pandas as pd
from django.http import JsonResponse
import threading

from django.apps import apps
from vehicledataanalysisinterfaceapi.utils.DataPreProcessing import zeroVelocityProcessing2
from vehicledataanalysisinterfaceapi.utils.DrawMap import drawMap, baseDBSCANMapNoiseReduction, kalman_filter
from vehicledataanalysisinterfaceapi.utils.DrivingBehaviorScore import DrivingBehaviorScore, Static_Behavior
from vehicledataanalysisinterfaceapi.utils.response.responsejava import datapreProcessingcallback

# Create your views here.

# 设置javaWeb基础路径
javaFrontUrl = apps.get_app_config('vehicledataanalysisinterfaceapi').javawebpath
# csv文件保存路径
csvSavePath = apps.get_app_config('vehicledataanalysisinterfaceapi').filesavepath


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
    file_obj = request.FILES.get("file")
    df = pd.read_csv(file_obj)
    df = baseDBSCANMapNoiseReduction(df)  # DBSCAN降噪
    df = kalman_filter(df, 2.0)  # 基于卡尔曼滤波进行平滑曲线
    # df = correctionOfTrajectoryBaiDu(df)  # 调用百度接口进行绑路
    savepath = drawMap(df)
    request_data = {"code": 200, "message": "请求成功", "path": savepath}
    return JsonResponse(request_data, status=200, charset="utf-8")


def trafficStatistics(request):
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
    def process_data():
        Static_Behavior(df)
        res["preprocessingState"] = 2
        datapreProcessingcallback(res)

    # 创建并启动新线程
    thread = threading.Thread(target=process_data)
    thread.start()

    request_data = {"code": 200, "message": "请求成功", }
    return JsonResponse(request_data, status=200, charset="utf-8")
