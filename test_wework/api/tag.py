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

    def add_tag(self):
        data = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_name": "group_name",
                "order": 1,
                "tag": [{
                    "name": "tag_name_1",
                    "order": 1
                }]
            }
        }

        return self.send_api(data)

    def get_tag(self):
        data = {
            "method": "POST",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {
                "access_token": self.token
            },
            "json": {
                "group_name": "group_name",
                "order": 1,
                "tag": [{
                    "name": "tag_name_1",
                    "order": 1
                }]
            }
        }
        pass

    def delete_tag(self):
        pass

    def update_tag(self):
        pass
