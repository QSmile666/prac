import requests


class TestWeworkApi:
    def test_wework_api(self):
        corpid = "ww6c619306416691d9"
        corpsecret = "2nWlaax4KBCNZZ9N0GNw1LhkpZx3qfBcKLKMlCj02O8"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        res = requests.get(url=url)
        print(res.json())
        token = res.json()["access_token"]
        assert res.json()["errcode"] == 0

        # 创建成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        body = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "department": [1, 12, 15],
            "email": "zhangsan@gzdev.com",
        }

        res = requests.post(url=url, json=body)
        print(res.json())
        assert res.json()["errcode"] == 0

        # 查看成员
        userid = "zhangsan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
        res = requests.get(url=url)
        print(res.json())
        assert res.json()["errcode"] == 0

        # 删除成员
        userid = "zhangsan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}"
        res = requests.get(url=url)
        print(res.json())
        assert res.json()["errcode"] == 0

    def test_getMembers(self):
        pass
