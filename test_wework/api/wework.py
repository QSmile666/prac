# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
import requests

from test_wework.api.base_api import BaseApi


class WeWork(BaseApi):
    corpid = "ww6c619306416691d9"

    def get_token(self, secret):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": self.corpid,
                "corpsecret": secret
            }
        }

        return self.send_api(data)["access_token"]
        # # 解包，不定长，还可以将key value转为url="XXX"；①满足必填字段的需求； ②无限扩展  字典的好处，python的独有特性
        # return requests.get(**data)
        # # self.token = res.json()["access_token"]
        # # # print(self.token)
        # # return self.token
