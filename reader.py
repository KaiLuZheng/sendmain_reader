#!/usr/bin/python3

from crapData import checkEOS
from sendmaillib import sendEmail

import json
import time

if __name__ == '__main__':
    count = 1
    while True: 
        print('start')
        eosline = checkEOS() 
        body = eosline['name'] + ':' + str(eosline['close'])
        sendEmail(body)

        print('end:%d'%count)
        count = count + 1
        time.sleep(5)

