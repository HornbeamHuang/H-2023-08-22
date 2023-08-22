"""
Author:Hornbeam
product:PyCharm
prpject:H-2023-08-22
name:DoRedis
user:Administrator
日期:2023/08/22 13:54
-------------------------------------
"""
from redis import Redis


class MyRedis:

    def __init__(self, number=0):
        # TODO 指定数据库
        self.r = Redis(host='172.18.5.43', port=6390, password='admin@yoc.tech', db=number)

    def get_token(self, name='test_oqhz'):
        token = self.r.get(f'atmp:token:{name}').decode('utf-8')
        return token

    def set_token(self, name, value):
        self.r.set(f'atmp:token:{name}', value)


if __name__ == '__main__':
    print(MyRedis().get_token())
