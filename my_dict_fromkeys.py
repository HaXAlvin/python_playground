from typing import Callable
keys = ["good", "bad"]


datas = dict.fromkeys(keys, list())
for value in datas.values():
    print(id(value))  # 139849248784712 139849248784712


def my_fromkeys(keys, default: Callable = lambda: None):
    return {key: default() for key in keys}
datas = my_fromkeys(keys, list)
for value in datas.values():
    print(id(value))  # 139849248809032 139849248809736
