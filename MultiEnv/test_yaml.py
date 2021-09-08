import yaml


# 将json内容转换为yaml格式的内容
def test_yaml():
    data = {
        "method": "POST",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
        "params": {
            "access_token": "self.token"
        },
        "json": {
            "group_name": "group_name",
            "order": 1,
            "tag": [{
                "name": "tag_name",
                "order": 1
            }]
        }
    }

    with open("data_addTag.yaml", "w") as f:
        yaml.safe_dump(data=data, stream=f)
