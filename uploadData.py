from time import sleep

import requests

upload_url = "http://devtest.ibr.cc:20317/upload/v1/custom"


# username = 'dataview_acc2'
# token = 'fe0046420e859cb3'

# username = 'dataview_2.2'
# token = '858696d0f9d0ecf9'

username = 'App_test'
token = 'db0589a5ded005ac'

datasource = 'custom.data'
headers = {
    'username': username,
    'token': token,
    'datasource': datasource
}
body = {
    "TAbLEName": "table5",
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



for i in range(1, 2):
    r = requests.post(url=upload_url, json=body, headers=headers)
    r.content.decode("utf-8")
    print(r.json())
    print(r.text)
    print("发送次数：", i)
    sleep(1)
