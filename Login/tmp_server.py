import schema
from fastapi import FastAPI
from pymongo import errors
from pymongo import MongoClient
import traceback
import pymongo

app = FastAPI()

def makeDB():
    try:
        client = MongoClient('127.0.0.1', 27017);
        # make database
        db = client['login']

        # make collection
        loginInfo = db['loginInfo']

        # create unique index
        loginInfo.create_index('loginId', unique=True)

        # example
        # loginInfo.insert_one({'loginId': 'admin', 'loginPassword': '1234'})

    except errors.DuplicateKeyError:
        pass
    except Exception:
        print(traceback.format_exc())

    return loginInfo


loginInfo = makeDB()


@app.post('/loginInfoModel')
async def receiveloginInfo(data: schema.loginInfoModel):
    data = dict(data)

    if data['kind'] == "signUp":
        result = loginInfo.find_one({'loginId': data['loginId']})
        if result is None:
            del(data['kind'])
            loginInfo.insert_one(data)
            print("회원 가입 완료되었습니다.")
        else:
            print("이미 있는 아이디 입니다.")

    elif data['kind'] == "signIn":
        result = loginInfo.find_one({'loginId': data['loginId'], 'loginPassword': data['loginPassword']})

        if result is None:
            print("회원 정보가 없습니다.")
        else:
            print("http://61.254.240.172:30000")