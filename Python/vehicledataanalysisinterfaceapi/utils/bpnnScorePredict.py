import pandas as pd
from matplotlib import pyplot as plt
from sklearn import preprocessing
import torch
import torch.nn as nn
import numpy as np
from torchsummary import summary
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# 定义一个BP神经网络模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(16, 5)  # 第一个全连接层，输入为16个特征，输出5个神经元
        self.fc2 = nn.Linear(5, 3)  # 第二个全连接层，输入为5个神经元，输出2个目标变量

    def forward(self, x):
        x = torch.sigmoid(self.fc1(x))  # 第一个全连接层的输出使用sigmoid激活函数
        x = self.fc2(x)  # 第二个全连接层不使用激活函数
        return x


# 训练的时候把 Django关闭 要不然路径不对
def bpnnPredict():
    # 设置使用cuda
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # 创建模型实例
    model = Net().to(device)
    summary(model, (1, 16))

    # 定义损失函数和优化器
    criterion = nn.MSELoss()  # 均方误差损失函数
    optimizer = torch.optim.SGD(model.parameters(), lr=2)  # 随机梯度下降优化器，学习率为0.01

    # 导入数据
    df1 = pd.read_excel('moudle/vehicle_clustered_new.xlsx', 0)
    # 进行数据归一化
    df1 = df1.iloc[:, :]
    min_max_scaler = preprocessing.MinMaxScaler()
    df0 = min_max_scaler.fit_transform(df1)
    df0 = df0.astype('float32')
    df = pd.DataFrame(df0, columns=df1.columns)
    x = df.iloc[:, :-3]
    y = df.iloc[:, -3:]
    # 划分训练集测试集
    cut = 20  # 取最后cut=20条为测试集
    x_train, x_test = np.array(x.iloc[:-cut]), np.array(x.iloc[-cut:])  # 列表的切片操作，X.iloc[0:2400，0:7]即为1-2400行，1-7列
    y_train, y_test = np.array(y.iloc[:-cut]), np.array(y.iloc[-cut:])

    for epoch in range(10000):  # 迭代训练10000次
        inputs = torch.from_numpy(x_train).to(device)
        targets = torch.from_numpy(y_train).to(device)

        # 前向传播
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # 反向传播和优化
        optimizer.zero_grad()  # 清空梯度
        loss.backward()  # 反向传播
        optimizer.step()  # 更新权重

        if epoch % 1000 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, 10000, loss.item()))

    optimizer = torch.optim.SGD(model.parameters(), lr=0.019)  # 随机梯度下降优化器，学习率为0.01

    for epoch in range(10000):  # 迭代训练10000次
        inputs = torch.from_numpy(x_train).to(device)
        targets = torch.from_numpy(y_train).to(device)

        # 前向传播
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # 反向传播和优化
        optimizer.zero_grad()  # 清空梯度
        loss.backward()  # 反向传播
        optimizer.step()  # 更新权重

        if epoch % 1000 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, 10000, loss.item()))



    with torch.no_grad():
        inputs = torch.from_numpy(x_test).to(device)
        targets = torch.from_numpy(y_test).to(device)
        outputs = model(inputs)
        predicted = torch.round(outputs)  # 将输出四舍五入到最接近的整数
        y_test = torch.round(targets)  # 将真实值四舍五入到最接近的整数
        accuracy = accuracy_score(predicted.cpu().numpy(), y_test.cpu().numpy())
        precision = precision_score(predicted.cpu().numpy(), y_test.cpu().numpy(), average='micro')
        recall = recall_score(predicted.cpu().numpy(), y_test.cpu().numpy(), average='micro')
        f1 = f1_score(predicted.cpu().numpy(), y_test.cpu().numpy(), average='micro')
        print('Accuracy: {:.4f}, Precision: {:.4f}, Recall: {:.4f}, F1: {:.4f}'.format(accuracy, precision, recall, f1))

    # 保存模型
    torch.save(model.state_dict(), 'moudle/model.pth')

