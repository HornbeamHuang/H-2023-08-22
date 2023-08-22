"""
Author:Hornbeam
product:PyCharm
prpject:H-2023-08-22
name:project_path
user:Administrator
日期:2023/08/22 11:09
-------------------------------------
"""
# -*- coding:utf-8 -*-
import os
import time

path = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
# 日志路径
now = time.strftime('%Y-%m-%d')
time_path = now + '.txt'
log_path = os.path.join(path, 'logs', time_path)

# 配置文件路径
config_path = os.path.join(path, 'common', 'conf', 'case_option.ini')
# print(config_path)

# 测试用例目录
cases_path = os.path.join(path, 'cases')

# 测试报告目录
report_path = os.path.join(path, 'reports')

# 用例数据目录
cases_data_path = os.path.join(path, 'data', 'cases.yaml')
# cases_data_path = os.path.join(path, 'data', 'cases.xlsx')
