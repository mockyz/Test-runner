# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     ontid_api
   Description :
   Author :        patrick
   date：          2019/7/10
-------------------------------------------------
   Change Activity:
                   2019/7/10:
-------------------------------------------------
"""
from core.client import HttpClient

__author__ = 'patrick'


class Login(HttpClient):
    method = "POST"
    req_url = "{{url31}}/web/v1/users/phone-login"
    req_body = {"data": "kTDYU1s3JAFIvTz38PkN5ZJJHOSeDJDab7h5TSg4U6oN76e/xrS+5ehGHR7q7t+AA6YdNYAOJbs2Vj+gcMgucNLu6t3XkxB7PJ7B56jWid/"
                        "Zy5RWLs3HHLBNRxUIrnDwCIBNhvEttuWMCOouk0j7RqA1FF2FFWgSBFjkZHTgqY8sR4GcmFo8wCIa5eESTv0H2eUIPw=="}
    headers = {
        'Secure-Key': 'HFriOp27CnMxnR/6uxH7t9VMRBHReJn0n2v+ZiA+QXjLFZoRZJk5DgM83KRiNbYnKY96kmnjrHghKcjUgK2KLtvgFzQupzWLtnQm2hB49viKT3+c3hvLV0VpeEVbAr/QvjsAFVHJe/5iuvBvMSTVcYYZ766H6xOnrPLzBQi7NTo=',
        'Accept': 'application/json', 'Content-Type': 'application/json'}


class CheckPhoneExist(HttpClient):
    method = "GET"
    req_url = "http://139.219.136.188:10331/web/v1/users/phones/check-existed?phone=86*17157727684"
    req_body = {}
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'ggjfhf'}


class SendResetPasswordVerificationCode(HttpClient):
    method = "POST"
    req_url = "{{url31}}/web/v1/users/phone/reset-password-verification-code"
    req_body = {'mode': 'raw',
                'raw': '{\n    "data": "ueXokQ3v3CRxn7xCHzUOhJr/b0bT8ntpxmenAg2WeQcopWMoUQZbMcq3xsQK2JcKnsJRF4a4mftNUWjhCv+2M2XazP2DYqzUaNqQ/dNmCszAkcn86FN5Ow9wCkoy4G/FVTGzHa11nTvRt5ecqz1mHg=="\n}'}
    headers = {'Content-Type': 'application/json',
               'Secure-Key': 'Ioo0sMzj1xOp1nTdOwdta8IJiJobREDaWEYZlBhhBGn6TTwxlxzcwlfuWRO6zFxBVcw4MPWfVyXbTw9okxQD7oh0CJVBKr04AKjUfHJjcgiXB5vbe73NojuQsJ7KSQYBbvAE6lxSctv9BZxo7YNt+Qreyppwnn21xQMUqTawDPw=',
               'Accept': 'application/json'}


class ResetPassword(HttpClient):
    method = "POST"
    req_url = "{{url31}}/web/v1/users/phone-reset-password"
    req_body = {'mode': 'raw',
                'raw': '{\n    "data": "/+sHghZlZEfWGxoSUfR5ZanMC01PrTrX2LQ+nkmB4beVk++UC63xY83Z3EqBCV0sIA1bAtqsKDyISK1W49EESxSBwbFz20GqJ+rstBI9hwnEpr1VMMx957oFgkXnM0Rd5JxfUCKmMFfxqz3jB7l4BxES2HiChdQvxaXsEes1DuCGMfeRuSX6g9WFEZ+zkzTJ480eJqPnJmPjgzXFEGCaZSg10g=="\n}'}
    headers = {'Content-Type': 'application/json',
               'Secure-Key': 'ljKx2p6jXopg+br5OCjZksk9qMF4P49D3mLtI8FmP+FdQt5IB4PFnrZBLFgXLKs6AeJRJlENsUbrdLe8FCPtO6AoMQd9Na5Sl6PjZLQIy3OUJpgkBXbfgElg0ot1OeiNmkoqQyPr2iPwHx8MkrKdvH65v9kJQre843BdMckVcvM=',
               'Accept': 'application/json'}


class PhoneProvider(HttpClient):
    method = "POST"
    req_url = "{{url31}}/web/v1/ontid/register/phone/provider"
    req_body = {'mode': 'raw',
                'raw': '{"data":"1BW841jSc/0+S984gGKRd7AnBDpJ9NhAG+qYwBO+FQrDS7g9i3liCb9RIfhAYxx1+bNazI4R0moBoxS6qvtNEQet0FKxf4BgI38WtkbZCpBR54v4nuDI18sLotTQIB4IymOskDqdNOHCUB+PRnI1aRyHpA92HimWO7jxckVuki0="}'}  # -*- coding: utf-8 -*-


class Register(HttpClient):
    method = "POST"
    req_url = "{{url31}}/web/v1/users/phone-register"
    req_body = {
        "data": "w5Dck3HV+Q13bIveKqn+T94J5Ul760sNrt9VftufKY13LOI0G5jOBwRWR2eKB/FCggWArlP075Wb5n9eDnL0VdOUOaG1lGEOZsygM0InEx4S3qFGovO1HuDV9bRMHXuLQWa450crx8Rd/5TTQ69flH0kG2HxP7DYLzdg+Il06EFkBhOVsPvNKhANgWGObO8Z0AVZQ8Nv70ocD2JBWQ=="}
    headers = {'Content-Type': '{{contentType}}', 'Accept': '{{Accept}}',
               'Secure-Key': 'drqv8KQf0yZEbnAFEb1dw0PRaNSpXxLETBegulsBLMlqc+In3gVDSMw/ffFM1l3wm04Aeo6JeuoIy8M+01PQxjAYuTMuaRJ3neiCo5d3G0z0+TzytuN/BJpNLo6JDAzT28BgcCNuH5Nx7AqMm45MFr4WRjNJb8EpyRZ0gqm8g3s='}


class SendRegistrationVerificationCode(HttpClient):
    method = "POST"
    req_url = "{{url31}}/web/v1/users/phones/register-verification-code"
    req_body = {"data":
                    "QPXLhB23R/EEtEIwtT6iDROctiFHX0gZcOBYCtaaWfJoFdwCTlDHNrqkq+LR7BSP1YyR4jKTwkVGFzpZ/HDT2/dFQxCNLw7aLYaWYeVK5tMD4v6QfeS+IAYVnmJDsPULnZyooa8eJDlEPWvGWjPXCg=="}
    headers = {'Content-Type': '{{contentType}}',
               'Secure-Key': 'lF2/zvYIdMrhj+X7MSSg0KWcNn2OPSh3EXpYug3EpOa7GmxnPQR7TZwFN6PaV2q9iUHv1YUSfiILkOTx0LNpKRkrU3uyBCkAW954DNew/E41Rh8CU8nWLbzAllBGgj1089y0cOv0Lq9qOb+Yyo7Ck2ZZ5fjMMmprTw97vt/p1Ew=',
               'Accept': '{{Accept}}'}


class CheckRegistered(HttpClient):
    method = "GET"
    req_url = "http://139.219.136.188:10331/web/v1/users/phones/check-registered?phone=86*17157727684"
    req_body = {}
    headers = {'Origin': 'ggjfhf', 'Content-Type': 'application/x-www-form-urlencoded'}


