from MultiEnv import env_demo


class TestAPI:
    data = {
        "method": "POST",
        "url": "http://devtest.ibr.cc:20392/upload/v1/custom",
        "headers": {
            'username': 'App_test',
            'token': 'db0589a5ded005ac',
            'datasource': 'custom.data'
        },
        "payload": {
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
                    "name": "a应用",
                    "value": 97
                },
                {
                    "name": "c应用",
                    "value": 72
                },
                {
                    "name": "b应用",
                    "value": 54
                },
                {
                    "name": "a应用",
                    "value": 63
                },
                {
                    "name": "立购台",
                    "value": 57
                }
            ]
        }
    }

    def test_send(self):
        api = env_demo.API()
        res = api.send(self.data)
        print(res.text)
