import yaml


# 将json内容转换为yaml格式的内容
def test_yaml():
    env = [
        ("yyaa", "yyaa-1"),
        ("opp", "oppa")
    ]

    with open("env.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)
