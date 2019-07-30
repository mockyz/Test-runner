# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     candybox_api
   Description :
   Author :        patrick
   date：          2019/7/12
-------------------------------------------------
   Change Activity:
                   2019/7/12:
-------------------------------------------------
"""
from core.client import HttpClient

__author__ = 'patrick'

DOMAIN_KEY="candybox"


class Login(HttpClient):
    method = "POST"
    req_url = "/api/v2/login"
    domain = DOMAIN_KEY
    req_body = {
        "nationalCode": "+86",
        "mobile": "18801096079",
        "password": "11111111"
    }
