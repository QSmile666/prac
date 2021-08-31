# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
import requests


class BaseApi:
    def send_api(self, req: dict):
        # 使用 request 完成多请求的改造（post, get, put等方法）
        return requests.request(**req).json()
