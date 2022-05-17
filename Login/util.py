import schema
from network import *


def signUp(data: dict):
    if data['kind'] == "signUp":
        result = sendData(data)
        print("util: ", result)