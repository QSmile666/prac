import yaml


# 将json内容转换为yaml格式的内容
def test_yaml():
    env = {
        "default": "test2",
        "devtest": {
            "test2": "20317",
            "test3": "20392",
        }
    }
    with open("env.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)
