import time
import traceback
import requests
import redisService
import json
import hashlib


class Payload:
    def __init__(self):
        self.loginInfo = {
            'kind': None,
            'loginId': None,
            'loginPassword': None,
        }


# DB: 8000, cache: 6379
HOST = 'http://127.0.0.1:{port}/{uri}'


def sendData(data: dict):
    url = HOST.format(port="8000", uri="loginInfoModel")
    result = requests.post(url=url, json=data)
    content = result.content.decode('utf-8')

    if result.status_code == 200:
        if content == "false":
            return False
        elif content == "true":
            return True
        else:
            return content
    else:
        return False
