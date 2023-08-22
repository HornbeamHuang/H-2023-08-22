"""
Author:Hornbeam
product:PyCharm
prpject:H-2023-08-22
name:logger
user:Administrator
日期:2023/08/22 11:18
-------------------------------------
"""
# -*- coding:utf-8 -*-
import logging
from common.public import project_path
from common.public.read_ini import Configuration


class MyLog:
    def __init__(self):
        self.logger_level = Configuration(project_path.config_path).read_str('LOG', 'logger_level')
        self.file_level = Configuration(project_path.config_path).read_str('LOG', 'file_level')
        self.file_name = Configuration(project_path.config_path).read_str('LOG', 'file_name')
        self.formatter = Configuration(project_path.config_path).read_str('LOG', 'formatter')
        self.log_name = project_path.log_path

    def my_log(self, level, msg):
        my_logger = logging.getLogger(self.file_name)
        my_logger.setLevel(self.logger_level)
        formatter = logging.Formatter(self.formatter)
        fh = logging.FileHandler(self.log_name, encoding='utf-8')
        fh.setLevel(self.file_level)
        fh.setFormatter(formatter)
        ch = logging.StreamHandler()
        ch.setLevel(self.file_level)
        ch.setFormatter(formatter)

        # 对接
        my_logger.addHandler(fh)
        my_logger.addHandler(ch)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)


if __name__ == '__main__':
    p = MyLog()
    p.error('睡觉啦！！！')
