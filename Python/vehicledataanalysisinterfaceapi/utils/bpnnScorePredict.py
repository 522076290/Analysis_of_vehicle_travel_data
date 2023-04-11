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


# 设置使用cuda
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 创建模型实例
model = Net().to(device)
summary(model, (1, 16))

# 定义损失函数和优化器
criterion = nn.MSELoss()  # 均方误差损失函数
optimizer = torch.optim.SGD(model.parameters(), lr=2)  # 随机梯度下降优化器，学习率为0.01

# 导入数据
df1 = pd.read_excel('vehicle_clustered_new.xlsx', 0)
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

# 测试模型
# with torch.no_grad():
#     inputs = torch.from_numpy(x_test).to(device)
#     targets = torch.from_numpy(y_test).to(device)
#     outputs = model(inputs)
#     test_loss = criterion(outputs, targets)
#     mse_loss = nn.MSELoss()(outputs, targets)
#     mae_loss = nn.L1Loss()(outputs, targets)
#     print('Test Loss: {:.4f}, MSE Loss: {:.4f}, MAE Loss: {:.4f}'.format(test_loss.item(), mse_loss.item(),
#                                                                          mae_loss.item()))

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
torch.save(model.state_dict(), 'model.pth')



# 将特征转换成张量并放到设备上
# features = torch.tensor(
#     [0.869565, 1.000000, 0.433333, 0.397163, 0.334677, 1.000000, 1.000000, 0.000000, 0.000000, 0.500000, 0.046829,
#      0.403061, 1.000000, 0.361461, 1.000000, 0.077038], dtype=torch.float32).to(
#     device)
# with torch.no_grad():
#     output = model(features)
#     output_first_element = output.index_select(0, torch.tensor([0]).to(device))
#     output_second_element = output.index_select(0, torch.tensor([1]).to(device))
# print(output_first_element.item())
# print(output_second_element.item())
#
# # 将归一化后的数据还原回原始数据
# df1_inverse = min_max_scaler.inverse_transform([[0.869565, 1.000000, 0.433333, 0.397163, 0.334677, 1.000000, 1.000000, 0.000000, 0.000000, 0.500000, 0.046829,
#      0.403061, 1.000000, 0.361461, 1.000000, 0.077038,output_first_element.item(), output_second_element.item()]])
#
# print(df1_inverse.astype(int))


# # 加载模型
# model = Net().to(device)
# model.load_state_dict(torch.load('model.pth'))
#
# # 设置模型为评估模式
# model.eval()
#
# # 输入数据进行预测
# with torch.no_grad():
#     output = model(torch.from_numpy(np.array(x)).to(device))
#     output = output.cpu().numpy()
#
# # 将输出转换为 numpy 数组
# prediction = output
#
# # 拼接数据
# x_with_prediction = np.concatenate((x, prediction), axis=1)
#
# # 将归一化后的数据还原回原始数据
# np.set_printoptions(threshold=np.inf)
# x_with_prediction_rounded = np.round(min_max_scaler.inverse_transform(x_with_prediction)).astype(int)
# print(x_with_prediction_rounded)