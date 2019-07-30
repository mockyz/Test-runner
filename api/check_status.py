# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     check_status
   Description :
   Author :        patrick
   date：          2019/6/25
-------------------------------------------------
   Change Activity:
                   2019/6/25:
-------------------------------------------------
"""
import json
import time

import requests

__author__ = 'patrick'
count = 0
with open('all_requests.txt', 'r') as fd:
    lines = fd.readlines()
    for line in lines:
        if (len(line.replace("\n", "")) > 0):
            data = json.loads(line)

            if data['result'] is not None:
                count = +1
                req_url = "https://api-ropsten.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash=" + \
                          data['result']['tx_hash']
                response = requests.get(req_url)
                print(data['result']['tx_hash'] + ":" + response.text)
                time.sleep(1)

print(count)