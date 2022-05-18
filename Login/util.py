from redisService import *
from network import *


class Util:
    def __init__(self):
        self.rediss= redisService()

    def signIn(self, data):
        if data['kind'] == "signIn":
            result = self.rediss.signIn(data)

            if result is False:
                return sendData(data)
            else:
                self.rediss.reInsertValue(data)
                return "http://61.254.240.172:30000"
        else:
          return False

    def signUp(self, data):
        if data['kind'] == "signUp":
            result1 = sendData(data)

            if result1 is not None:
                result2 = self.rediss.signUp(data)
                return True

            return False
        else:
            return False