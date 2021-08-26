import requests


class TestWeworkApi:
    corpid = "ww6c619306416691d9"
    corpsecret = "2nWlaax4KBCNZZ9N0GNw1LhkpZx3qfBcKLKMlCj02O8"

    def setup(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        res = requests.get(url=url)
        print(res.json())
        self.token = res.json()["access_token"]
        assert res.json()["errcode"] == 0
        return self.token

    def test_wework_api(self):
        # 删除成员
        userid = "zhangsan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        res = requests.get(url=url)
        print(res.json())
        # assert res.json()["errcode"] == 0

        # 创建成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        create_data = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "department": [1, 12, 15],
            "email": "zhangsan@gzdev.com",
        }

        res = requests.post(url=url, json=create_data)
        print(res.json())
        assert res.json()["errcode"] == 0

        # 查看成员
        # userid = "zhangsan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        res = requests.get(url=url)
        print(res.json())
        assert res.json()["errcode"] == 0

        # 更新成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        update_data = {
            "userid": userid,
            "name": "张三",
        }
        res = requests.post(url=url, json=update_data)
        print(res.json())
        assert res.json()["errcode"] == 0
