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
from wsgiref import headers

from core.client import HttpClient

__author__ = 'patrick'


class OntoServiceAPI(HttpClient):
    domain = "ontoservice"
    headers = {'ContentType': 'application/json', 'Accept': 'application/json'}


## chapter 2
# 用户注册OntId

class OntIdRegisterAPI(OntoServiceAPI):
    domain = "ontoservice2"
    req_url = "api/v1/ontpass/ontid/register"
    method = "POST"
    req_body = {
        "OwnerOntId": "",
        "TxnStr": ""
    }


class OntidRegisterWithInviteCode(OntoServiceAPI):
    method = "POST"
    req_url = "api/v2/ontpass/ontid/register"
    req_body = {
        "ont_id": "当前默认 ONT ID",
        "txn": "",
        "invitation_code": "邀请码"
    }


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
    req_url = "/api/v1/onto/email/verificationcode/verification"
    query_params = ["email", "code"]


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
    params = {
        "currency": "ont",
        # "goaltype": "USD",
        "amount": 100
    }


class GetAppVersion(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/appclientversion/query"
    query_params = ["platform", "currentVersionCode"]


class GetAppConfig(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/appconfig/query"


class GetSystemInfo(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/onto/SystemMessage/GetAfterTimeWithLanguages"
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
    query_params = ["phonenumber", "code"]


class GetTokenList(OntoServiceAPI):
    method = "GET"
    req_url = "api/v1/onto/token/{type}"
    query_params = ["pageNum", "pageSize"]
    params = {
        "type": "oep4",
        "pageNum": 0,
        "pageSize": 10
    }


class GetTokenListByTokenHashOrName(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/token/list"
    query_params = ["pageNum", "pageSize", "name", "contract"]
    params = {
        "name": "",
        "pageNum": 0,
        "pageSize": 10,
        "contract": ""
    }


class GetERC20List(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/erc-20"
    query_params = ["pageNum", "pageSize"]
    params = {
        "pageNum": 0,
        "pageSize": 10
    }


class GetERC20ByToken(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/onto/erc-20/list"
    params = {
        "name": "name",
        "contract": "",
        "pageNum": 0,
        "pageSize": 12
    }
    query_params = params.keys()


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


# 第二次版本提交
class QueryDeviceCode(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/devicecode/regain"
    req_body = {"OwnerOntId": "",
                "Signature": {
                    'Value': '1231sscsdasdadad123312312',
                    'Algorithm': 'ESDCA',
                    'PublickeyId': 'did:ont:TA5YqmVWNKTaiZfnWd9oAzbnShMmqTxStd#keys-1'
                }
                },
    headers = {'ContentType': 'application/json', 'Accept': 'application/json'}


class RegistOntId(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/ontid/register"
    req_body = {'OwnerOntId': "", 'TxnStr': ""}
    headers = {'ContentType': 'application/json', 'Accept': 'application/json'}


# 资产转账自付
class TransferSelfPay(OntoServiceAPI):
    method = "POST"
    req_url = "/v2/ontoservice/transactions?action=selfPay"
    req_body = {
        "amount": 1,
        "asset_name": "ont",
        "from_address": "AP6DUbMX2BvsT7TDhX6g9WGcEK6pCP4VB6",
        "to_address": "AP6DUbMX2BvsT7TDhX6g9WGcEK6pCP4VB6",
        "transaction_hash": "",
        "transaction_str": "",
        "gas": "0.01"
    }


# 资产转账自付API(新版)
class TransferServerPay(OntoServiceAPI):
    method = "POST"
    req_url = "/v2/ontoservice/transactions?action=serverPay"
    req_body = {
        "amount": 1,
        "asset_name": "ont",
        "from_address": "AP6DUbMX2BvsT7TDhX6g9WGcEK6pCP4VB6",
        "to_address": "AP6DUbMX2BvsT7TDhX6g9WGcEK6pCP4VB6",
        "transaction_hash": "",
        "transaction_str": "",
        "gas": "0.01"
    }


# 资产转账
# OntoPass服务提供的旧版本接口
# 用户资产转账。app端代付还是自付看后台配置
class AssetTransfer(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/asset/transfer"
    req_body = {"SendAddress": "ATc5gXifZQ1C1gMCoRMrGEvhWxhvQ5w1RG",
                "ReceiveAddress": "AX2kRrJWLqdcrC9fq7CUswPjdXz6hGLBRe",
                "AssetName": "ont",
                "Amount": 1,
                "TxnStr": ""}


class ClaimConfirm(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/claim/confirm"
    req_body = {"OwnerOntId": "", "DeviceCode": "", "ClaimId": "", "TxnHash": "", "ConfirmFlag": True}
    headers = {'ContentType': 'application/json', 'Accept': 'application/json'}


# 未使用
class WebsocketMessage(OntoServiceAPI):
    method = "websocket"
    req_url = "url：ws://47.96.138.224:5053/api/v1/ontpass/pending/message"
    req_body = {"Action": "VerifyIdentity", "OwnerOntId": "did:ont:TCGusnHW325YddAxxB49MmvZMTNG5EHGtj",
                "DeviceCode": "device1JH7629cncmdj13", "BeginTime": "20180102", "EndTime": "20180202"}
    headers = {'ContentType': 'application/json', 'Accept': 'application/json'}


class QueryTransferInfo(OntoServiceAPI):
    method = "GET"
    req_url = "/v2/ontoservice/transactions"
    query_params = ["address", "asset_name", "end_time"]
    params = {
        "address": "",
        "asset_name": "",
        "end_time": ""
    }


class QueryPoints(OntoServiceAPI):
    method = "GET"
    req_url = "api/v2/ontpass/points/{ontId}"
    params = {
        'ontId': "123"
    }


class UpdatePoints(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v2/ontpass/points"
    req_body = {"address": "", "ont_id": "", "amount": "", "coin_type": "",
                "device_code": ""}


class NoticeQuery(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/notice/query/{pageSize}/{pageNumber}"
    req_body = {"OwnerOntId": "", "DeviceCode": "", "NoticeType": "Claim", "Status": [1, 2, 4], "BeginTime": "20171223",
                "EndTime": "20181229"}


class CreateInvitation_Code(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v2/ontpass/invitation-code"
    req_body = {"ont_id": "", "device_code": ""}


# ----未使用
class UpdateDdo(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/ddo/update"
    req_body = {"OwnerOntId": "", "DeviceCode": "", "TxnStr": "", "ClaimId": ""}


class VerifyInvitationCode(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v2/ontpass/invitation-code/{invitation-code}/check"
    req_body = {}
    query_params = ["invitation-code"]


class QueryBrief(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/claim/brief/query"
    req_body = {
                   'OwnerOntId': '', 'DeviceCode': '', 'ClaimContext': '', 'Status': [1, 2], 'BeginTime': '20171223',
                   'EndTime': '20171229'},


class QueryClaim(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/claim/query"
    req_body = {"OwnerOntId": "", "DeviceCode": "", "ClaimId": "", "ClaimContext": "", "Status": ""}


class LocalizationConfirm(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/localization/confirm"
    req_body = {"OwnerOntId": "", "DeviceCode": "", "ClaimId": ""}


# 用户所有已托管可信声明获取
class QueryEntrustedClaim(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/entrustedclaim/query"
    req_body = {"OwnerOntId": "", "DeviceCode": ""}


# 用户可信声明认证记录查询
class RecordClaim(OntoServiceAPI):
    method = "POST"
    req_url = "api/v1/ontpass/claim/record"
    req_body = {"ownerOntId": "", "deviceCode": "", "pageNumber": 1, "pageSize": 10, "language": "EN"}


# 机构托管可信声明
class EntrustmentClaim(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/ontpass/claim/entrustment"
    req_body = {"IssuerOntId": "did:ont:TWsN8G8AphJxzgWYwHqvYqgntBf5DzBvEX", "ClaimList": [
        {"Description": "employment authentication",
         "Id": "0086d7808785c1221521f7bf8fe47328679b5ad9c47848e7c65d762a093a0f46",
         "Context": "claim:employment_authentication", "OwnerOntId": "did:ont:TJEYyZHzTjemEytKCNsEvwjPzsXSYc8910",
         "CreateTime": "2019-08-12 HH:mm:ss", "IssuerName": "onchain", "IssuerOntId": "did:ont:Tzsd12313cscsdc",
         "TxnHash": "cc0d69ad45eb292b9535e2fec00653d28e74954f744b9ca75be6751e09d2b542",
         "EncryptedOrigData": "533328a29c8f32ca006f2aa20a90e021026959208816dba7bb"}],
                "Signature": {"Value": "1231sscsdasdadad123312312", "Algorithm": "ESDCA",
                              "PublickeyId": "did:ont:TA5YqmVWNKTaiZfnWd9oAzbnShMmqTxStd#keys-1"}}


# 获取场景方信息API
class QueryThirdpartyInfo(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/ontpass/thirdparty/info/{language}"
    req_body = {"OntId": "did:ont:A17j42nDdZSyUBdYhWoxnnE5nUdLyiPoK3", "Lan": "EN", "ReqContext": "authtemplate_kyc01",
                "Sig": "AXFqt7w/xg+IFQBRZvucKXvTuIZaIxOS0pesuBj1IKHvw56DaFwWogIcr1B9zQ13nUM0w5g30KHNNVCTo04lHF0="}


class AuthConfirm(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/ontpass/auth/confirm"
    req_body = {"OntId": "did:ont:AA75Qaq2ju14rhr6obDLWYBQjry7b8ku4p",
                "DeviceCode": "device1223424",
                "AuthFlag": True,
                "ThirdPartyOntId": "did:ont:AJJzVj5tZjgwvhvdeZmQwjUEDtqhEoPfxU",
                "ClaimIds": [],
                "ClaimContexts": []}


class QueryAuthenticationRecord(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/ontpass/authentication/record?langauge=EN"
    req_body = {"OntId": "did:ont:A17j42nDdZSyUBdYhWoxnnE5nUdLyiPoK3", "DeviceCode": "device122344323", "PageNumber": 1,
                "PageSize": 10, }


class CreateSharedWallet(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/ontpass/SharedWallet/create"
    req_body = {
        "sharedWalletAddress": "AJz9tLVtXDZtsb7sc2Kbz2GNBmtQNXzMnk",
        "sharedWalletName": "cjf gang",
        "totalNumber": 2,
        "requiredNumber": 2,
        "coPayers": [{'name': 'cjf',
                      'publickey': '023056a1a1350bd806a7db3c5270364d4c499a5006980ebd8105e62d7228236c8d',
                      'address': 'Aa86sFYswFn1TJh8Mbgbrqa2XKV8qznYGh'},
                     {'name': 'gang',
                      'publickey': '02ce28dd00d8b75a2ace915cb04197104b73257be9e338e8cedcbbf31e9844bb33',
                      'address': 'ATbxAz1cVe81zx7RXL4Ty7b1s5UXh48Szn'}]
    }


# 根据共享钱包地址获取共享钱包信息
class QueryShareWalletInfo(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/ontpass/SharedWallet/getBySharedWalletAddress?sharedWalletAddress={sharedWalletAddress}"
    req_body = {}
    query_params = ["sharedWalletAddress"]


# 创建需要共享转账的交易
# 调用该API，可以提交需要转账的交易给服务器
class CreateTransfer(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/ontpass/SharedTransfer/create"
    req_body = {
        "sendAddress": "AJz9tLVtXDZtsb7sc2Kbz2GNBmtQNXzMnk",
        "receiveAddress": "AW9H22ZLuNAceA4qwjDJcLq9uQ7NhNmVMf",
        "assetName": "ont",
        "amount": 100,
        "gasLimit": 20000,
        "gasPrice": 500,
        "transactionIdHash": "632da2cee43e0d07801856d8b5d51c505e225dc647a985d3984055b745d4162c",
        "transactionBodyHash": "00d141b99d45f401000000000000204e000000000000233aec97cfec848d56d01bb5c97cf6e28f693dc67900c66b14233aec97cfec848d56d01bb5c97cf6e28f693dc66a7cc8149d9e0165f657b6f62eb6494c37ef158d80ccafc66a7cc80864000000000000006a7cc86c51c1087472616e736665721400000000000000000000000000000000000000010068164f6e746f6c6f67792e4e61746976652e496e766f6b650000",
        "coPayers": [
            {
                "name": "cjf",
                "address": "Aa86sFYswFn1TJh8Mbgbrqa2XKV8qznYGh"
            },
            {
                "name": "gang",
                "address": "ATbxAz1cVe81zx7RXL4Ty7b1s5UXh48Szn"
            }

        ]
    }


# 签名同意转账
# 调用该API，同意待签名的转账
class SignTransfer(OntoServiceAPI):
    method = "POST"
    req_url = "/api/v1/ontpass/SharedTransfer/sign"
    req_body = {
        "transactionIdHash": "zxzasdfkasdhfqwerasdf",
        "signedAddress": "qwerqwerqewr",
        "signedHash": "qweroiuyasdfkjhzxcvnasdfkh"
    }


# 获取共享钱包Signing的交易列表
# 调用该API，可以根据对应地址的共享钱包信息
class QuerySigningTransfer(OntoServiceAPI):
    method = "GET"
    req_url = "/api/v1/ontpass/SharedTransfer/listSigningBeforeTime?sharedAddress={sharedAddress}&assetName={assetName}&beforeTimeStamp={beforeTimeStamp}"
    query_params = ["sharedAddress", "assetName", "beforeTimeStamp"]
    headers = {'ContentType': 'application/json', 'Accept': 'application/json'}


# 代付提取Ong
class Claimong_txs(OntoServiceAPI):
    method = "POST"
    req_url = "/v2/ontoservice/transactions/claimong-txs"
    req_body = {'claimong_data': 'string', 'claimong_hash': 'string', 'transfer_data': 'string',
                'transfer_hash': 'string'
                }
