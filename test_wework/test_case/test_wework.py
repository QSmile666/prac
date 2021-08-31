# !/usr/bin/env python
# _*_ coding:utf-8 _*_
# @author: zhenhualee
from test_wework.api.wework import WeWork


class TestWeWork:
    def test_getToken(self):
        secret = "xSDP_WU3oOxVWX3gFCM22B1KPftYbEXDW2uDOkszN9w"
        print(WeWork().get_token(secret))
