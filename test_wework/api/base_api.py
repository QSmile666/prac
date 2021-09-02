# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
from pprint import pprint

import requests
from jsonpath import jsonpath


class BaseApi:
    def send_api(self, req: dict):
        # 使用 request 完成多请求的改造（post, get, put等方法）
        res = requests.request(**req)
        pprint(res.json())
        return res.json()

    @staticmethod
    def jsonpath(json, expr):
        return jsonpath(json, expr)
