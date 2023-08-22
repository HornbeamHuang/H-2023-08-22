"""
Author:Hornbeam
product:PyCharm
prpject:H-2023-08-22
name:sendDingTalk
user:Administrator
日期:2023/08/22 11:37
-------------------------------------
"""
import hmac
import hashlib
import base64
import urllib.parse
import requests
import time
from common.public import project_path
from common.public.read_ini import Configuration


class DingTalk:

    def __init__(self):
        self.url = Configuration(project_path.config_path).read_str('DingTalk', 'DingUrl')
        self.secret = Configuration(project_path.config_path).read_str('DingTalk', 'secret')

    def get_stamp(self):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return {"sign": sign, "timestamp": timestamp}

    def send_msg(self, msg, link):
        data = {
            "msgtype": "actionCard",
            "actionCard": {
                "title": "H-2023-08-22",
                "text": msg,
                "singleTitle": "查看报告",
                "singleURL": link
            },
            "at": {
                "atMobiles": [],
                "isAtAll": False
            }
        }
        if self.secret:
            params = self.get_stamp()
        else:
            params = None
        response = requests.post(url=self.url, json=data, params=params)
        return response


if __name__ == '__main__':
    ding = DingTalk()
    ding.send_msg("msg", "http://www.baidu.com")
    print("钉钉信息发送成功.......")
