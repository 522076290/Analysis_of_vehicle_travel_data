import os
from django.apps import AppConfig


class VehicledataanalysisinterfaceapiConfig(AppConfig):
    name = 'vehicledataanalysisinterfaceapi'
    # 地图数据保存路径
    mapsavepath = os.path.abspath('../resourcesavepath/mapresource')
    # 天气数据保存路径
    weatherdata = os.path.abspath('../data/附件2-气象数据.csv')
    # java 前端地址 用于获取csv文件
    javawebpath = 'http://localhost/dev-api'
    # java后台地址 用于回调接口
    javabasepath = 'http://localhost:8080'
    # 修改后的数据保存路径
    filesavepath = 'D:/ruoyi/uploadPath'

