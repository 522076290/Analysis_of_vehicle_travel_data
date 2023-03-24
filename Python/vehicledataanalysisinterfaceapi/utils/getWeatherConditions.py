# coding:utf-8
import json
import urllib.request
import sys
import pandas as pd
import datetime
import os

from django.apps import apps


# 将天气情况的描述拆分出来,返回一个集合
def splitWeatherTag(conditions):
    result = []
    if '转' in conditions:
        tmpTag = conditions.strip().split('转')
        for tag in tmpTag:
            if '-' in tag:
                result.extend(tag.strip().split('-'))
                continue
            result.append(tag)

    elif '-' in conditions:

        tmpTag = conditions.strip().split('-')
        for tag in tmpTag:
            if '转' in tag:
                result.extend(tag.strip().split('转'))
                continue
            result.append(tag)
    else:
        result.append(conditions)
    result = set(result)
    # print(result)
    return result


# 根据气象数据返回字典，key为省市区，日期组成的列表，value为conditions属性
def genLocation_Date_Weather_Dict():
    # weatherFile=os.getcwd()+"/Data/附件2-气象数据.csv"
    weatherFile = apps.get_app_config('vehicledataanalysisinterfaceapi').weatherdata
    # 有中文的文件一定要设置编码
    df = pd.read_csv(weatherFile, encoding='gbk', low_memory=False)
    rows = df.shape[0]
    resultDict = {}
    for i in range(0, rows):
        item = df.iloc[i]
        tmpProvince = item['province']
        tmpCity = item['prefecture_city']
        tmpCounty = item['county']
        condition = item['conditions']
        tmpDate = datetime.datetime.strptime(item['record_date'], '%d/%m/%Y').date()
        resultKey = (tmpProvince, tmpCity, tmpCounty, tmpDate)
        resultDict[resultKey] = condition

    return resultDict



def getWeatherConditionByCoordinateAndDate(df, weatherDict):
    """
    基于百度地图API下的经纬度信息来解析地理位置信息,并获取对应时间地点的天气情况
    curDate必须为%d/%m/%Y 形式
    :param df: 车辆行驶数据
    :param weatherDict: 天气字典
    :return:
    """
    item = df.iloc[0]
    lng = item['lng']
    lat = item['lat']
    DateandTime = datetime.datetime.strptime(item['location_time'], '%Y-%m-%d %H:%M:%S')
    curDate = DateandTime.date()  # 提取日期

    # 转换坐标api,将WGS84坐标转换为BD09II
    transUrl = 'http://api.map.baidu.com/geoconv/v1/?coords=' + str(lng) + ',' + str(
        lat) + '&from=1&to=5&ak=YWWVWk2KHmCyMFta3D0cCZttGborOrkt'
    tranReq = urllib.request.urlopen(transUrl)
    tranResult = tranReq.read().decode('utf-8')
    # 返回的是str类型，使用json读取
    tranResult = json.loads(tranResult)
    tranStatus = tranResult.get('status')
    if tranStatus != 0:
        # 转换失败
        print("coodinate transform error!")
        sys.exit(1)
    coodinate = tranResult.get('result')[0]  # 返回的是列表，使用[0]提取，为字典类型
    lng = coodinate['x']
    lat = coodinate['y']
    # 使用转换后的经纬度查询省市区
    # api文档
    url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak={}&output=json&coordtype=wgs84ll&location={},{}'.format(
        "YWWVWk2KHmCyMFta3D0cCZttGborOrkt", lat, lng)
    req = urllib.request.urlopen(url)  # json格式的返回数据
    res = req.read().decode("utf-8")  # 将其他编码的字符串解码成unicode
    resultJson = json.loads(res).get('result')
    address = resultJson.get('addressComponent')

    # 获取坐标对应的省市区
    province = address.get('province').strip('省')
    city = address.get('city').strip('市')
    district = address.get('district')[:-1]

    tmpKey = (province, city, district, curDate)
    if tmpKey in weatherDict:
        return splitWeatherTag(weatherDict[tmpKey])
    # 找不到对应地点的天气情况，返回字符串集合'未知'
    # print("未知")
    return ["未知"]