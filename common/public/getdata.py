"""
Author:Hornbeam
product:PyCharm
prpject:H-2023-08-22
name:getdata
user:Administrator
日期:2023/08/22 11:12
-------------------------------------
"""
from common.public.read_ini import Configuration
from common.public import project_path


class GetData:
    timeout = 8.0
    base_url = Configuration(project_path.config_path).read_str('URL', 'url')
    button = Configuration(project_path.config_path).read_str('CASE', 'button')
    headers = {
        'appId': 'jljs',
        'platform': 'jljs',
        'deviceId': '9267',
        'imei': '',
        'deviceBrand': 'vivo',
        'deviceInfo': 'vivo_V2001A',
        'sourceCode': 'app',
        'version': '1.5.1',
        'os': 'android',
        'androidId': 'dc0de9ff14a64f20',
        'deviceImei': '',
        'channelCode': 'oi35vu',
        'oaid': '826ec7b020667b5026c8ecc42c166eaa2fc2273fcd8c54396c302627af429dcb'
    }
    # 盲盒ID
    id = ''
    # 提货地址Id
    addrId = ''
    # 提货商品id
    goodsId = ""
    pick_id = ''
    # 商品订单号
    outTradeNo = ''
    # 替换商品id
    replaceId = ''
    # 取消订单ID
    orderId = ''
    # 商城类目ID
    categoryId = ''
    # 兑换商品id
    exchangeId = ''
    # 支付方式
    pay_type = ''


if __name__ == '__main__':
    print(GetData().base_url)
    # 18583168310
