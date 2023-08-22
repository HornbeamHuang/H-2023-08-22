"""
Author:Hornbeam
product:PyCharm
prpject:H-2023-08-22
name:read_ini
user:Administrator
日期:2023/08/22 11:10
-------------------------------------
"""
# -*- coding:utf-8 -*-
from configparser import ConfigParser
from common.public import project_path


class Configuration:
    def __init__(self, file_name):
        self.cf = ConfigParser()
        self.cf.read(file_name, encoding='utf-8')

    def read_str(self, section, option):
        value = self.cf.get(section, option)
        return value

    def read_else(self, section, option):
        value = self.cf.get(section, option)
        return eval(value)


if __name__ == '__main__':
    p = Configuration(project_path.config_path)
    print(p.read_str('DingTalk', 'Secret'))
