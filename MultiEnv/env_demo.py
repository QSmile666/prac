import requests
import yaml


class API:
    env = yaml.safe_load(open("env.yaml"))

    def send(self, data: dict):
        data["url"] = str(data["url"]).replace("20392", self.env["devtest"][self.env["default"]])
        r = requests.request(method=data["method"], url=data["url"], json=data["payload"],
                             headers=data["headers"])
        return r

