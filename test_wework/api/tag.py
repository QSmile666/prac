# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
from test_wework.api.base_api import BaseApi
from test_wework.api.wework import WeWork


class Tag(BaseApi):
    secret = "xSDP_WU3oOxVWX3gFCM22B1KPftYbEXDW2uDOkszN9w"

    # 初始化方法
    def __init__(self):
        self.token = WeWork().get_token(self.secret)

    def add_tag(self, tag_name):
        data = self.load("../api/tag.add.yaml")
        data["params"]["access_token"] = self.token
        data["json"]["tag"][0]["name"] = tag_name

        return self.send_api(data)

    def get_tag(self):
        data = self.load("../api/tag.get.yaml")
        print(data)
        data["params"]["access_token"] = self.token
        return self.send_api(data)

    def delete_tag(self, tag_id):
        data = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "tag_id": [
                    tag_id
                ]
            }
        }
        return self.send_api(data)

    def update_tag(self, tag_id, name):
        data = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": tag_id,
                "name": name
            }
        }
        return self.send_api(data)
