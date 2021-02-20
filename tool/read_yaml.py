import os
import yaml
from config import BASE_PATH


def read_yaml(system, file, filename):
    # 动态文件路径
    file_path = BASE_PATH + os.sep + "data" + os.sep + system + os.sep + file + os.sep + filename
    # 定义空列表 组装测试数据
    arr = []
    # 获取文件流
    with open(file_path, "r", encoding="utf-8") as f:
        # 遍历 调用yaml.safe_load(f).values()方法
        for datas in yaml.safe_load(f).values():
            arr.append(tuple(datas.values()))
        # 返回 结果
        return arr


if __name__ == '__main__':
    print(read_yaml("admin", "scripts", "create_doctor.yaml"))
