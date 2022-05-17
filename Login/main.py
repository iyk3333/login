from network import *
from util import *


if __name__=='__main__':
    data = dict()
    data['kind'] = 'signUp'
    data['loginId'] = 'catty33353'
    data['loginPassword'] = '4321'

    sendData(data)