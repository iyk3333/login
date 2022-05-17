import traceback
import requests


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
    # cache 에 있는 지 확인
    url = HOST.format(port="8000", uri="loginInfoModel")

    result = requests.post(url=url, json=data)

    if result.status_code == 200:
        return True
    else:
        return False
