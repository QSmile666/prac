from time import sleep

import requests

# pre
# upload_url = "http://118.194.54.254:20063/upload/v1/custom"
# huawei_test
upload_url = "http://10.10.20.30:9997/upload/v1/custom"

username = 'lzh_test'
token = '246ea9150b6536bb'

# username = 'apm_test'
# token = 'c1708bb3ce45d936'

# username = 'livedemo'
# token = 'be0c2c58c643ae06'
datasource = 'custom'
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
            "name": "a应用",
            "value": 97
        },
        {
            "name": "uup应用",
            "value": 72
        },
        {
            "name": "qq应用",
            "value": 54
        },
        {
            "name": "yy应用",
            "value": 63
        },
        {
            "name": "立购台",
            "value": 57
        }
    ]
}

for i in range(1, 10000):
    r = requests.post(url=upload_url, json=body, headers=headers)
    r.content.decode("utf-8")
    print(r.json())
    print(r.text)
    print("发送次数：", i)
    sleep(3)
