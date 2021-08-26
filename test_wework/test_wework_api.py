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

    def test_member_api(self):
        # 删除成员
        userid = "zhangsan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        res = requests.get(url=url)
        print(res.json())
        # assert res.json()["errcode"] == 0

        # 创建成员
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        create_memberData = {
            "userid": "zhangsan",
            "name": "张三",
            "alias": "jackzhang",
            "department": [1, 12, 15],
            "email": "zhangsan@gzdev.com",
        }

        res = requests.post(url=url, json=create_memberData)
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
        update_memberData = {
            "userid": userid,
            "name": "张三",
        }
        res = requests.post(url=url, json=update_memberData)
        print(res.json())
        assert res.json()["errcode"] == 0

    def test_department_api(self):
        # 删除部门
        departId = 10
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={departId}"
        res = requests.get(url=url)
        print(res.json())
        assert res.json()["errcode"] == 0

        # 创建部门
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        create_departData = {
            "name": "yy研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 10
        }
        res = requests.post(url=url, json=create_departData)
        print(res.json())
        assert res.json()["errcode"] == 0

        # 查看部门
        departId = 10
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id={departId}"
        res = requests.get(url=url)
        print(res.json())
        assert res.json()["errcode"] == 0

        # 修改部门
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        update_departData = {
            "id": departId,
            "name": "yys研发中心",
            "name_en": "yysRDGZ",
            "parentid": 1,
            "order": 1
        }
        res = requests.post(url=url, json=update_departData)
        print(res.json())
        assert res.json()["errcode"] == 0
