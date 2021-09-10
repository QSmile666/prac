# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
from pprint import pprint
from string import Template

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    def send_api(self, req: dict):
        # 使用 request 完成多请求的改造（post, get, put等方法）
        res = requests.request(**req)
        pprint(res.json())
        return res.json()

    @classmethod
    def jsonpath(cls, json, expr):
        return jsonpath(json, expr)

    @classmethod
    def load(cls, path):
        with open(path, "r") as f:
            return yaml.safe_load(f)

    @classmethod
    def template(cls, path, data, opera=None):
        with open(path, "r") as f:
            if opera is None:
                return yaml.load(Template(f.read()).substitute(data))
            else:
                # load函数将数据转化为列表或字典  dump是转储给一个字符串
                # Template可以将字符串的格式固定下来，是属于string中的一个类
                return yaml.load(Template(yaml.dump(yaml.load(f)[opera])).substitute(data))
