# 用于回调java程序
import json

import requests
from django.apps import apps
from django.http import JsonResponse

# 设置java后台基础路径
javaBackUrl = apps.get_app_config('vehicledataanalysisinterfaceapi').javabasepath


# 数据预处理回调
def datapreProcessingcallback(response):
    """
    数据预处理回调
    :param response: 用于响应的数据
    :return:
    """
    # 定义请求URL和数据
    url = javaBackUrl + "/vehicledrivingdata/vehicledrivingdatacallback/preprocessing-callback"
    # 将数据转换为JSON格式并发送POST请求
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, data=json.dumps(response), headers=headers)
    # 处理响应
    if response.status_code == 200:
        result = response.json()
        return JsonResponse(result, status=200)
    else:
        error = {'message': '请求失败'}
        return JsonResponse(error, status=400)


# 驾驶行为统计回调
def datastatisticscallback(response):
    """
    驾驶行为统计回调
    :param response: 用于响应的数据
    :return:
    """
    # 定义请求URL和数据
    url = javaBackUrl + "/vehicledrivingdata/vehicledrivingdatacallback/preprocessing-callback"
    # 将数据转换为JSON格式并发送POST请求
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, data=json.dumps(response), headers=headers)
    # 处理响应
    if response.status_code == 200:
        result = response.json()
        return JsonResponse(result, status=200)
    else:
        error = {'message': '请求失败'}
        return JsonResponse(error, status=400)


def drawmapcallback(response):
    """
    地图生成完回调
    :param response: 用于响应的数据
    :return:
    """
    # 定义请求URL和数据
    url = javaBackUrl + "/vehicledrivingdata/vehicledrivingdatacallback/draw-map-callback"
    # 将数据转换为JSON格式并发送POST请求
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, data=json.dumps(response), headers=headers)
    # 处理响应
    if response.status_code == 200:
        result = response.json()
        return JsonResponse(result, status=200)
    else:
        error = {'message': '请求失败'}
        return JsonResponse(error, status=400)


# 地图文件上传回调
def uploaddrawmap(savemappath):
    upload_url = javaBackUrl + '/common/upload'
    # 打开文件
    with open(savemappath, 'rb') as f:
        # 构造请求参数
        files = {'file': ('map.html', f)}
        # 发送POST请求，上传文件
        response = requests.post(upload_url, files=files)
        res = json.loads(response.content)
    return res["fileName"]
