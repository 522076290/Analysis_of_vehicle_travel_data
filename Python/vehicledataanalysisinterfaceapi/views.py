from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
from vehicledataanalysisinterfaceapi.utils.DataPreProcessing import zeroVelocityProcessing
from vehicledataanalysisinterfaceapi.utils.DrawMap import drawMap, baseDBSCANMapNoiseReduction, kalman_filter , correctionOfTrajectoryBaiDu

# Create your views here.



def datapreprocessingapi(request):
    """
    数据预处理接口
    获取request 传入的csv文件 进行数据预处理后存储到指定位置 并返回处理结果
    :param request:  post请求
    :return: 返回Json数据
    """
    file_obj = request.FILES.get("file")
    df = pd.read_csv(file_obj)
    df2 = zeroVelocityProcessing(df)
    df2.to_csv("df2.csv")
    request_data = {"code": 200, "message": "请求成功"}
    return JsonResponse(request_data)


def drawmapapi(request):
    """
    根据传入的行车数据绘制出行车路线图  内部进行数据的降噪处理
    :param request:  post请求
    :return: 返回Json数据
    """
    file_obj = request.FILES.get("file")
    df = pd.read_csv(file_obj)
    df = baseDBSCANMapNoiseReduction(df)  # DBSCAN降噪
    df = kalman_filter(df, 1.0)  # 基于卡尔曼滤波进行平滑曲线
    # df = correctionOfTrajectoryBaiDu(df)  # 调用百度接口进行绑路
    savepath = drawMap(df)
    request_data = {"code": 200, "message": "请求成功", "path": savepath}
    return JsonResponse(request_data)