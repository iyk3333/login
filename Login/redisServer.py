import redis
import json
import hashlib
import time


class redisService:
    def __init__(self):
        self.result = redis.Redis(host="127.0.0.1", port=6379, password="1234", decode_responses=True)

    # redis의 key값 sha256 만들기
    def makeHash(self, loginId: str) -> str:
        return hashlib.sha256(loginId.encode()).hexdigest()

    def findValue(self, key: str) -> dict:
        return self.result.get(name=key)

    def insertValue(self, key: str, value: dict):
        self.result.set(name=key, value=json.dumps(value))

    def reInsertValue(self, value: dict):
        hashValue = self.makeHash(value['loginId'])
        value['timestamp'] = time.time()
        self.insertValue(key=hashValue, value=value)

    # 로그인
    def signIn(self, data):
        result = self.findValue(self.makeHash(data['loginId']))

        if result is None:
            return False
        else:
            return True

    # 회원 가입 시 redis에도 저장
    def signUp(self, data):
        hashValue = self.makeHash(data['loginId'])
        data['timestamp'] = time.time()
        self.insertValue(key=hashValue, value=data)