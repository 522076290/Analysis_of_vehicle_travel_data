import os
from django.apps import AppConfig


class VehicledataanalysisinterfaceapiConfig(AppConfig):
    name = 'vehicledataanalysisinterfaceapi'
    mapsavepath = os.path.abspath('../resourcesavepath/mapresource')
    weatherdata = os.path.abspath('../data/附件2-气象数据.csv')

