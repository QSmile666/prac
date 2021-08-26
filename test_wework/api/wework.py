# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
import requests

from test_wework.api.base_api import BaseApi


class WeWork:
    corpid = "ww6c619306416691d9"
    corpsecret = "2nWlaax4KBCNZZ9N0GNw1LhkpZx3qfBcKLKMlCj02O8"

    def get_token(self, secret):
        secret = self.corpsecret
        data = {
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": self.corpid,
                "corpsecret": secret
            }
        }
        # 解包，不定长，还可以将key value转为url="XXX"；①满足必填字段的需求； ②无限扩展  字典的好处，python的独有特性
        return requests.get(**data)
        # self.token = res.json()["access_token"]
        # # print(self.token)
        # return self.token
