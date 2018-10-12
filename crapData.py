#!/usr/bin/python3 


import urllib
import urllib.request
import logging
import json

headers = {} 
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/69.0.3497.81 Chrome/69.0.3497.81 Safari/537.36'

def reqCore(url):
    req = urllib.request.Request(url, headers = headers)
    try:
        res = urllib.request.urlopen(req)
        return res
    except Exception as e:
        logging.error(e)
        res = ''
        return (res)


def checkEOS():
    url = 'https://www.hbg.com/-/x/general/index/constituent_symbol/detail'
    res = reqCore(url)
    sjson = json.loads(res.read())
    return sjson['data']['symbols'][1]


if __name__ == '__main__':
    logging.basicConfig(level = logging.DEBUG)
    logging.debug(checkEOS())


