import requests


class TestWechat:
    def test_wechat(self):
        corpid = "ww6c619306416691d9"
        corpsecret = "2nWlaax4KBCNZZ9N0GNw1LhkpZx3qfBcKLKMlCj02O8"
        res = requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
        print(res.json())
        token = res.json()["access_token"]
        assert res.json()["errcode"] == 0

    def test_getMembers(self):
        pass
