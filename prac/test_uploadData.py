import requests


class TestDemo:
    upload_url = "http://devtest.ibr.cc:20317/upload/v1/custom"
    username = 'App_test'
    token = 'db0589a5ded005ac'
    datasource = 'custom.data'
    headers = {
        'username': username,
        'token': token,
        'datasource': datasource
    }
    body = {
        "TAbLEName": "table1",
        "FIeLDValueType": [
            {
                "fieldName": "metric",
                "valueType": "string"
            },
            {
                "fieldName": "value",
                "valueType": "doubleSum"
            }
        ],
        "DaTaS": [
            {
                "name": "MyApplication",
                "value": 100
            },
            {
                "name": "MyApplication",
                "value": 97
            },
            {
                "name": "MyApplication",
                "value": 72
            },
            {
                "name": "aaa",
                "value": 54
            },
            {
                "name": "MyApplication",
                "value": 63
            },
            {
                "name": "立购台",
                "value": 57
            }
        ]
    }

    def test_uploadData(self):
        r = requests.post(url=self.upload_url, data=self.body, headers=self.headers)
        print(r.json())
        assert r.status_code == 200
