import traceback
import requests


class Payload:
    def __init__(self):
        self.loginInfo = {
            'loginId': None,
            'loginPassword': None,
        }


HOST = 'http://127.0.0.1:8000/{uri}'


def sendData(data: dict):
    url = HOST.format(uri="loginInfoModel")
    result = requests.post(url=url, json=data)

    print(result)

    if result.status_code == 200:
        return True
    else:
        return False
