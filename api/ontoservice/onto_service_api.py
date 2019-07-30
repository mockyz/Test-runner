# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     onto_service_api
   Description :
   Author :        patrick
   date：          2019/7/29
-------------------------------------------------
   Change Activity:
                   2019/7/29:
-------------------------------------------------
"""
from core.client import HttpClient

__author__ = 'patrick'


class OntoServiceAPI(HttpClient):
    domain = "ontoservice"
    headers = {'ContentType': 'application/json', 'Accept': 'application/json'}


class SendEmailVerificationCode(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/onto/email/verificationcode/send"
    req_body = {
        "OwnerOntId": "did:ont:AWhbY6dKWvWYRyoYKNyfhm2MGnGuTns22Z",
        "DeviceCode": "device1263429723",
        "Email": "16672782277@163.com"
    }


class VerifyEmailCode(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/email/verificationcode/verification?email=""&code="""
    query_params = {
        "email": "email",
        "code": "code"
    }


class GetTrustAnchorList(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/onto/trustanchor/query"
    req_body = {
        "OwnerOntId": "",
        "DeviceCode": "",
        "PageNumber": 1,
        "PageSize": 10,
        "Language": "CN"
    }


class GetExchangeCurrency(OntoServiceAPI):
    method = "GET"
    req_url = "api/v1/onto/exchangerate/reckon/{currency}/{goaltype}/{amount}"


class GetAppVersion(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/appclientversion/query?platform={platform}&currentVersionCode={currentVersionCode}"


class GetAppConfig(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/appconfig/query"


class GetSystemINfo(OntoServiceAPI):
    method = "POST"
    req_url = "1+D9"
    req_body = {
        "AfterTime": 1427846724876,
        "languages": ["en", "cn"]
    }


class SendSMSVerificationCode(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/onto/sms/verificationcode/send"
    req_body = {
        "OwnerOntId": "did:ont:AWhbY6dKWvWYRyoYKNyfhm2MGnGuTns22Z",
        "DeviceCode": "device1263429723",
        "PhoneNumber": "86*18217008888"
    }


class VerifySMSCode(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/sms/verificationcode/verification"
    query_params = {
        "phonenumber": "86*123456789",
        "code": "code"
    }


class GetERC20List(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/erc-20?pageNum=0&pageSize=10"


class GetERC20ByToken(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/erc-20/list?name=&contract=&pageNum=1&pageSize=3"
    query_params = {
        "name": "name",
        "contract": "contract",
        "pageNum": 0,
        "pageSize": 12
    }


class AddNewERC20Token(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/onto/erc-20"
    req_body = {
        "tokenHash": "0x68566f399098555ad508d349d16f94aa83a7067e",
        "tokenName": "BAT",
        "symbol": "BAT",
        "decimals": 18,
        "icon": "http://172.168.3.60:8081/0x0d8775f648430679a709e98d2b0cb6250d2887ef.png"
    }


class ModifyERC20Token(OntoServiceAPI):
    method = "PUT"
    req_url = "/api/v1/onto/erc-20"
    req_body = {
        "tokenHash": "0x68566f399098555ad508d349d16f94aa83a7067e",
        "tokenName": "BAT",
        "symbol": "BAT",
        "decimals": 18,
        "icon": "http://172.168.3.60:8081/0x0d8775f648430679a709e98d2b0cb6250d2887ef.png"
    }
