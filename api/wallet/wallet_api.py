# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     wallet_api
   Description :
   Author :        patrick
   date：          2019/6/20
-------------------------------------------------
   Change Activity:
                   2019/6/20:
-------------------------------------------------
"""
from core.client import HttpClient

__author__ = 'patrick'

WALLET_SERVER = "WALLET_SERVER"


class WalletAPI(HttpClient):
    method = "POST"
    domain = WALLET_SERVER
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    def build_body(self):
        for k, v in self.params.items():
            if self.req_body.get(k) is not None:
                self.req_body[k] = v
            else:
                self.req_body.get('data')[0][k] = v


class BusinessOperStatusQuery(WalletAPI):
    req_url = "/api/v1/businessoperstatusquery"
    ## make sure the some variables with default values
    req_body = {
        "businessNo": ""
    }


class NewAccount(WalletAPI):
    """
    交易所开户接口
    """
    req_url = "/api/v1/newaccount"
    req_body = {
        "businessNo": "",
        "data": [
            {
                "coinType": ""
            }
        ]
    }


class ApplyForWithDrawal(WalletAPI):
    """
    出金依赖，申请出金
    """
    req_url = "/api/v1/applyforwithdrawal"
    req_body = {
        "batchId": "",
        "data": [
            {
                "businessNo": "",
                "coinType": "",
                "fromAddr": "",
                "data": [
                    {
                        "destAddr": "",
                        "sendAmount": ""
                    }
                ]
            }
        ]
    }


class WithdrawalBatchConfirm(WalletAPI):
    """
    出金批次确认发送
    """
    req_url = "/api/v1/withdrawalbatchconfirm"
    req_body = {
        "batchId": "${#TestCase#批次号}",
        "businessNo": "${#TestSuite#业务流水号}",
        "coinType": "${#TestCase#coinType}",
        "result": "${#TestCase#是否出金}"
    }


class QueryHistoryMsg(WalletAPI):
    """
    历史消息查询
    """
    req_url = "/api/v1/queryhistorymsg"
    req_body = {"msgId": "${#TestCase#消息ID}"}


class ExportAccount(WalletAPI):
    req_url = "api/v1/exportaccount"
    req_body = {
        "businessNo": "${#TestSuite#业务流水号}",
        "coinType": "${#TestCase#币种}"
    }


class QueryLedgerAmountBalance(WalletAPI):
    """
    查询冷钱包资金余额
    """

    req_url = "/api/v1/queryledgeramountbalance"
    req_body = {
        "businessNo": "${#TestSuite#业务流水号}",
        "data": [
            {
                "coldWalletAddr": "${#TestCase#地址}",
                "coinType": "${#TestCase#币种}"
            }
        ]
    }


class CheckDesAddrIsValid(WalletAPI):
    """
    检查出金目的地址是否有效
    """
    req_url = "/api/v1/checkdestaddrisvalid"
    req_body = {
        "businessNo": "${#TestSuite#业务流水号}",
        "destAddr": "${#TestCase#地址}",
        "coinType": "${#TestCase#币种}"
    }


class EmergencyStopStartSvr(WalletAPI):
    """
    紧急停止/启动服务
    """
    req_utl = "/api/v1/emergencystoporstartsvr"
    req_body = {
        "businessNo": "${#TestSuite#业务流水号}",
        "status": "${#TestCase#操作状态}",
        "OperType": "${#TestCase#操作类型}",
        "data": [
            {
                "coinType": ""
            }
        ]
    }


class ReconciliationDetails(WalletAPI):
    """
    获取该时间段内对账明细
    """
    req_url = "/api/v1/reconciliationdetails"
    req_body = {
        "businessNo": "${#TestSuite#业务流水号}",
        "reconciliationType": "${#TestCase#出入金类型}",
        "beginTime": "${#TestCase#开始时间}",
        "endTime": "${#TestCase#结束时间}",
        "format": "${#TestCase#格式}"
    }


class SetCollectThreshold(WalletAPI):
    """
    设置币种归集阈值
    """
    req_url = "/api/v1/setcollectthreshold"
    req_body = {
        "businessNo": "${#TestSuite#业务流水号}",
        "data": [
            {
                "coinType": "${#TestCase#币种}",
                "threshold": "${#TestCase#阈值}"
            }
        ]
    }


class ReportInCoins(WalletAPI):
    """
    上报入金状态
    """
    req_url = "/ngdes/api /wallet/v1/reportInCoins"
    req_body = {"msgId": "", "coinType": "", "hash": "", "fromAddr": "", "exchangeCoinAddr": "", "rechargeAmount": "",
                "rechargeTime": "", "rechargeStatus": ""}


class ReportOutCoinsDetail(WalletAPI):
    """
    上报入金状态
    """
    req_url = "/ngdes/api /wallet/v1/reportInCoins"
    req_body = {"code": "", "msgId": "", "message": ""}


class ReportOutCoinsStatus(WalletAPI):
    """
    上报入金状态
    """
    req_url = "/ngdes/api /wallet/v1/reportOutCoinsStatus"
    req_body = {"batchId": "", "data": "", "bussinessNo": "", "coinType": "", "fromAddr": "", "data": "",
                "destAddr": "", "sendAmount": ""}


class ReportRisk(WalletAPI):
    req_url = "/ngdes/api /wallet/v1/reportRisk"
    req_body = {"msgId": "", "coinType": "", "message": "", "riskCode": ""}


# 消息预备加密
# Hex 加密

"""
def s = context.expand( '${#TestCase#hex}' )
if (s == null || s.equals("")) {
        return null;
    }
    s = s.replace(" ", "");
    byte[] baKeyword = new byte[s.size() / 2];
    for (int i = 0; i < baKeyword.length; i++) {
        try {
            baKeyword[i] = (byte) (0xff & Integer.parseInt(s.substring(i * 2, i * 2 + 2), 16));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    try {
        s = new String(baKeyword, "UTF-8");
        new String();
    } catch (Exception e1) {
        e1.printStackTrace();
    }
    return s;
"""
