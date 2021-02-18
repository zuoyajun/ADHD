import logging.handlers
import os
import time
from config import BASE_PATH


class GetLogger:
    __logger = None

    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 设置日志器级别
            cls.__logger.setLevel(logging.INFO)
            file = BASE_PATH + os.sep + "log" + os.sep + "{}.log".format(time.strftime("%Y-%m-%d"))
            # 获取处理器 文件-以时间分割
            """
            filename:文件路径及文件名
            maxBytes:最大字节，1024 * 1024为1M，达到200M压缩
            backupCount:备份的日志数量(备份7个，多余的删除)
            encoding:编码格式
            """
            th = logging.handlers.RotatingFileHandler(filename=file,
                                                      maxBytes=1024 * 1024 * 200,
                                                      backupCount=7,
                                                      encoding="utf-8")

            # 设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s [%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)

            # 将格式器添加到处理器 文件
            th.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__logger.addHandler(th)
        return cls.__logger


if __name__ == '__main__':
    log = GetLogger.get_logger()
    for i in range(10000):
        log.info("测试打印日志日志日志日志日志日志日志")
