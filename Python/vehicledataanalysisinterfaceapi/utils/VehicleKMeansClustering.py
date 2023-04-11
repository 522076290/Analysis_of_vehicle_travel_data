import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_excel('vehicle.xlsx', 0)
data = df.iloc[:, -2:].values

# 设定聚类数量
k = 3

# 聚类
kmeans = KMeans(n_clusters=k, random_state=0).fit(data)

# 打印聚类中心
print(kmeans.cluster_centers_)

# 打印每个样本所属的聚类
print(kmeans.labels_)

# 添加聚类结果到原始数据中
df['cluster'] = kmeans.labels_

# 保存文件
df.to_excel('vehicle_clustered_new.xlsx', index=False)

# 可视化展示
plt.rcParams['font.family'] = 'SimHei'  # 设置中文字体为黑体
plt.scatter(data[:, 0], data[:, 1], c=kmeans.labels_)
plt.xlabel('安全模型得分')
plt.ylabel('节能模型得分')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=200, linewidths=3, color='r')
plt.show()
