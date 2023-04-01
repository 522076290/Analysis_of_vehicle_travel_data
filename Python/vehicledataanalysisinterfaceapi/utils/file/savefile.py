import os
import datetime


def save_file(fileName):
    # 获取当前日期
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # 创建保存文件的文件夹
    save_dir = os.path.join('D:', 'ruoyi', 'uploadPath', 'upload', str(year), f'{month:02}', f'{day:02}')
    os.makedirs(save_dir, exist_ok=True)

    # 生成文件名
    filename = f'my_file_{now.strftime("%Y%m%d%H%M%S")}.txt'
    filepath = filename

    return filepath
