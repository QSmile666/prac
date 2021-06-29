import requests


class API:
    env = {
        "default": "test2",
        "devtest": {
            "test2": "20317",
            "test3": "20392",
        }
    }

    def send(self, data: dict):
        data["url"] = str(data["url"]).replace("20392", self.env["devtest"][self.env["default"]])
        r = requests.request(method=data["method"], url=data["url"], json=data["payload"],
                             headers=data["headers"])
        return r
