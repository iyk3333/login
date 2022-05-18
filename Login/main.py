from util import *

'''
    signIn
        이미 있는 경우: 주소 리턴
        없는 경우: False 리턴
    signUp
        이미 있는 경우: False 리턴
        없는 경우: True 리턴
'''


if __name__=='__main__':
    data = Payload().loginInfo
    data['kind'] = 'signIn'
    data['loginId'] = 'iyk3333'
    data['loginPassword'] = '4321'


    util = Util()

    result = util.signIn(data)

    print("결과:", result)