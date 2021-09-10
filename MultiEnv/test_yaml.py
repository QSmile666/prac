import yaml


# 将json内容转换为yaml格式的内容
def test_yaml():
    data = {
        "method": "POST",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
        "params": {
            "access_token": "token"
        },
        "json": {
            "id": "tag_id",
            "name": "name"
        }
    }

    with open("data_updateTag.yaml", "w") as f:
        yaml.safe_dump(data=data, stream=f)
