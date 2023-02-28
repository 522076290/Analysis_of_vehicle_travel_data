import folium
from django.apps import apps
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
import seaborn as sns
from sklearn.neighbors import DistanceMetric
from pykalman import KalmanFilter
import urllib.request
import time
import json

# 设定卡尔曼滤波模型参数
kf = KalmanFilter(
    transition_matrices=np.eye(2),
    observation_matrices=np.eye(2),
    initial_state_mean=np.zeros(2),
    initial_state_covariance=np.ones((2, 2)),
    observation_covariance=np.eye(2),
    transition_covariance=0.1 * np.eye(2)
)



def drawMap(df):
    """
        :param df: 需要绘制地图的数据
        :return: 没有返回值
    """
    savemappath = apps.get_app_config('vehicledataanalysisinterfaceapi').mapsavepath + '\\map.html'
    m1 = folium.Map(location=[df['lat'].mean(), df['lng'].mean()], zoom_start=11)
    mydata1 = df.loc[:, ["lat", "lng"]].values.tolist()
    folium.PolyLine(mydata1, color='red').add_to(m1)
    m1.save(savemappath)
    return savemappath


def baseDBSCANMapNoiseReduction(df):
    """
            :param df: 需要绘制地图的数据
            :return: 返回降噪过后的数据集
    """
    sns.set()
    # 使用sklearn.neighbors 计算经纬度距离
    dist = DistanceMetric.get_metric('haversine')
    # 取出经纬度数据
    lonandlat = df[['lat', 'lng']].dropna(axis=0, how='all')
    # 转换经纬度为弧度
    df2 = np.radians(lonandlat)
    # 地球半径长度
    EARTH_RADIUS_KM = 6371.0088
    # 设置进制为米
    METERS = 1000.0
    # 一次无法处理大量数据 所以分批次处理 每次20000条记录
    m = 20000
    resultofclustering = []
    for r in [df2[i:i + m] for i in range(0, len(df2), m)]:  # 列表⽣成式
        distance_matrix = EARTH_RADIUS_KM * METERS * dist.pairwise(r)
        db = DBSCAN(eps=27, min_samples=3, metric='precomputed').fit_predict(distance_matrix)
        resultofclustering.extend(db)
        pass
    resultofclustering = np.array(resultofclustering)
    # 调用DBSCAN 使用fit训练
    labels = resultofclustering
    raito = len(labels[labels[:] == -1]) / len(labels)  # 计算噪声点个数占总数的比例
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)  # 获取分簇的数目
    df['label'] = labels
    df_filtered = df[df.label > -1]
    return df_filtered


def kalman_filter(df, obs_noise):
    """
    基于卡尔曼滤波的经纬度降噪
    :param df: 包含经纬度的数据框
    :param obs_noise: 观测噪声方差
    :return: 降噪后的经纬度数据框
    """
    # 将经纬度数据转换为二维数组形式
    obs = np.array(df[['lng', 'lat']])

    # 设定卡尔曼滤波模型的参数
    kf.observation_covariance = np.diag([obs_noise, obs_noise])
    kf.initial_state_mean = obs[0]
    kf.initial_state_covariance = np.diag([obs_noise, obs_noise])

    # 执行卡尔曼滤波
    filtered_state_means, filtered_state_covariances = kf.filter(obs)
    df_filtered = df.copy()
    df_filtered[['lng', 'lat']] = filtered_state_means

    return df_filtered


def correctionOfTrajectoryBaiDu(df):
    """
    将原始数据进行轨迹纠偏 使用百度轨迹纠偏接口
    需要三个参数 经度 纬度 时间戳
    请求地址： https://api.map.baidu.com/rectify/v1/track? //POST


    POST BODY中请求参数填写示例
    ak:<您的ak>
    point_list: [{"loc_time":1624295452,"latitude":36.2715924153,"longitude":120.401133898,"coord_type_input":"bd09ll"},
                {"loc_time":1624296515,"latitude":36.2411743783,"longitude":120.360663512,"coord_type_input":"bd09ll"}]
    rectify_option: need_mapmatch:1|transport_mode:driving|denoise_grade:1|vacuate_grade:1

    接口文档：https://lbs.baidu.com/index.php?title=webapi/guide/trackrectify

    :param df: 需要转换地址的数据
    """
    mydata1 = df.loc[:, ["lng", "lat", "location_time"]].values.tolist()  # 取出
    mydata2 = []
    mydata3 = []
    allpoints = []
    for indexs in mydata1:
        # 处理数据格式 对应请求接口
        indexs[2] = int(time.mktime(time.strptime(indexs[2], "%Y-%m-%d %H:%M:%S")))  # 将日期转换成时间戳
        middict = {"loc_time": str(indexs[2]), "latitude": str(indexs[1]), "longitude": str(indexs[0]),
                   "coord_type_input": "wgs84"}
        middict = json.dumps(middict)  # 转换dick的时候保存“” 接口格式必须完全和 point_list 一致
        mydata2.append(middict)
        pass

    # 一次只能处理2000条数据 所以将数据分组
    m = 2000
    for r in [mydata2[i:i + m] for i in range(0, len(mydata2), m)]:  # 列表⽣成式
        mydata3.append(r)
        pass

    for i in range(0,  len(mydata3)):
        url = 'https://api.map.baidu.com/rectify/v1/track?'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        }
        data = {
            'ak': 'YWWVWk2KHmCyMFta3D0cCZttGborOrkt',
            "point_list": str(mydata3[i]).replace("'", ''),  # 这里是去除 list的单引号
            "rectify_option": "need_mapmatch:1|transport_mode:driving|denoise_grade:2|vacuate_grade:2"
        }
        # post请求的参数 必须要进行编码
        data = urllib.parse.urlencode(data).encode('utf-8')
        # 请求对象的定制
        request = urllib.request.Request(url=url, data=data, headers=headers)
        # 模拟浏览器向服务器发送请求
        response = urllib.request.urlopen(request)
        # 获取响应的数据
        content = response.read().decode('utf-8')
        # 字符串转换成json对象
        obj = json.loads(content)
        # 检测请求状况 如果状态码不是0 说明请求失败
        status = obj['status']
        if status != 0:
            # 转换失败
            print("请求失败!")
            # 结束循环
            break
        # 取出纠偏后的信息
        points = obj['points']
        # 暂停1秒钟 百度QPS限制
        time.sleep(1)
        # 将每次获取的纠偏信息拼接
        allpoints.extend(points)

    # 保存纠偏后的轨迹
    offsetCorrectingAddress = pd.DataFrame(
        columns=['loc_time', 'latitude', 'longitude', 'speed', 'direction'])

    countnum = 1
    for indexs in allpoints:
        offsetCorrectingAddress.loc[countnum] = \
            [indexs.get("loc_time"), indexs.get("latitude"), indexs.get("longitude"), indexs.get("speed"),
             indexs.get("direction")]
        countnum += 1
    offsetCorrectingAddress.rename(columns={'latitude': 'lat', 'longitude': 'lng'}, inplace=True)
    return offsetCorrectingAddress