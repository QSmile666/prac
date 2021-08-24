import requests
from requests.auth import HTTPBasicAuth


class TestDemo:
    def test_oauth(self):
        url = "https://httpbin.testing-studio.com/basic-auth/yyy/123456"
        header = {"accept": "application/json"}
        r = requests.get(url=url, auth=HTTPBasicAuth("yyy", "123456"), headers=header)
        print(r.json())
        print(r.headers)
