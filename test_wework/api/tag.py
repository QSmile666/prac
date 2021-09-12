# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
from string import Template

from test_wework.api.base_api import BaseApi
from test_wework.api.wework import WeWork


class Tag(BaseApi):
    secret = "xSDP_WU3oOxVWX3gFCM22B1KPftYbEXDW2uDOkszN9w"

    # 初始化方法
    def __init__(self):
        self.token = WeWork().get_token(self.secret)

    def add_tag(self, **data):
        # data = self.load("../api/tag.add.yaml")
        # data["params"]["access_token"] = self.token
        # data["json"]["tag"][0]["name"] = tag_name

        data.update({'token': self.token})
        data = self.template("../api/tag.all.yaml", data, opera="add")
        return self.send_api(data)

    def get_tag(self, **data):
        # data = self.load("../api/tag.get.yaml")
        # print(data)
        # data["params"]["access_token"] = self.token
        data.update({"token": self.token})
        data = self.template("../api/tag.all.yaml", data, opera="get")
        return self.send_api(data)

    def delete_tag(self, **data):
        data.update({"token": self.token})
        data = self.template("../api/tag.all.yaml", data, opera="delete")
        return self.send_api(data)

    def update_tag(self, **data):
        data.update({"token": self.token})
        data = self.template("../api/tag.all.yaml", data, opera="update")
        return self.send_api(data)
