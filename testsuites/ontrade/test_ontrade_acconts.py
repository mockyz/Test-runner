# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     ontrade_acconts
   Description :
   Author :        patrick
   date：          2019/7/16
-------------------------------------------------
   Change Activity:
                   2019/7/16:
-------------------------------------------------
"""
from api.wallet import wallet_api

__author__ = 'patrick'



class TestOnTradeAccount:

    def test_create_address(self):

        api = wallet_api.NewAccount(params={
            "businessNo":0,
            "coinType":"ont"
        })

        response = api.invoke()
        print(response)
