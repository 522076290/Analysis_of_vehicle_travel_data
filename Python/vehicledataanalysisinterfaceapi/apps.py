import os
from django.apps import AppConfig


class VehicledataanalysisinterfaceapiConfig(AppConfig):
    name = 'vehicledataanalysisinterfaceapi'
    mapsavepath = os.path.abspath('../resourcesavepath/mapresource')
