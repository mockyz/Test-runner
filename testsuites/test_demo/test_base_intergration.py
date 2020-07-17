# -- coding: utf-8 --

# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_bnb_integration
   Description :
   Author :        patrick
   date：          2019/8/14
-------------------------------------------------
   Change Activity:
                   2019/8/14:
-------------------------------------------------
"""
import allure
import pytest
import logging
import json
from api.ontrade import ontrade_api as OnTradeAPI
from core.utils.assertpy import assert_that
from testsuites.test_demo.utils import *

__author__ = 'patrick'


class TestOntradeBase:

    def create_account(self, BaseConfig, inputs, expectedCode):
        api = OnTradeAPI.NewAccount() \
            .with_body_param("businessNo", BaseConfig.CoinType + business_no()) \
            .with_body_param("data", inputs)
        response = api.invoke()
        # 比较返回的code值与预期是否一致
        assert (response.get_response_attr("code") == expectedCode)
        # 返回的查询结果与地址数一致
        assert (len(response.get_response_attr("result")) == len(inputs))
        # 循环检查结果创建成功或失败，根据期待值
        for result in response.get_response_attr("result"):
            if result["exchangeCoinAddr"] != "":
                self.new_address = result["exchangeCoinAddr"]
            assert_that(result["exchangeCoinAddr"] == "" or expectedCode != 0, BaseConfig)

    def check_address_valid(self, BaseConfig, inputs, expectedResult):
        api = OnTradeAPI.CheckDesAddrIsValid() \
            .with_body_param("businessNo", BaseConfig.CoinType + business_no()) \
            .with_body_param("destAddr", inputs) \
            .with_body_param("coinType", BaseConfig.CoinType)
        response = api.invoke()
        logging.info(json.dumps(response.data))
        assert response.get_response_attr("result") == expectedResult["result"]
        assert response.get_response_attr("hasTx") == expectedResult["hasTx"]

    def query_balance(self, BaseConfig, inputs, expectedCode):
        api = OnTradeAPI.QueryLedgerAmountBalance() \
            .with_body_param("businessNo", BaseConfig.CoinType + business_no()) \
            .with_body_param("data", inputs)
        response = api.invoke()
        # 比较返回的code值与预期是否一致
        assert (response.get_response_attr("code") == expectedCode)
        # 返回的查询结果与地址数一致
        assert (len(response.get_response_attr("result")) == len(inputs) or expectedCode != 0)
        # 如果code为0，检查返回结果中的地址余额是否存在
        for result in response.get_response_attr("result"):
            assert (result["amount"] != "" and result["errorMessage"] == "" or expectedCode != 0)

    def set_collection_threshold(self, BaseConfig, inputs, expectedCode):
        api = OnTradeAPI.SetCollectThreshold() \
            .with_body_params(businessNo=BaseConfig.CoinType + business_no(), data=inputs)
        response = api.invoke()
        # 比较返回的code值与预期是否一致
        assert (response.get_response_attr("code") == expectedCode["code"])
        # 如果code为0，检查返回结果中的地址余额是否存在
        for index in range(0, len(response.get_response_attr("result"))):
            result = response.get_response_attr("result")[index]
            logging.info(result["resultCode"] == expectedCode["resCode"][index])
            assert (result["resultCode"] == expectedCode["resCode"][index])

    def apply_for_withdraw(self, BaseConfig, inputs, expectedCode):
        time.sleep(3)
        batchId = BaseConfig.CoinType + str(business_no())
        api = OnTradeAPI.ApplyForWithDrawal().with_body_params(batchId=str(batchId), data=inputs)
        response = api.invoke()
        assert (response.get_response_attr("code") == expectedCode["code"])
        # 记录出金批次号
        if response.get_response_attr("code") == '0':
            self.with_drawal_bacth.append((BaseConfig, batchId, {"code": 0}))

        # 根据需要是否直接取消出金
        api = OnTradeAPI.WithdrawalBatchConfirm().with_body_params(coinType=BaseConfig.CoinType,
                                                                   businessNo=BaseConfig.CoinType + business_no(),
                                                                   batchId=batchId,
                                                                   result="1")
        response = api.invoke()

        assert (response.get_response_attr("code") == expectedCode["code"])

    def confirm_withdraw(self, BaseConfig, inputs, expectedCode):
        api = OnTradeAPI.WithdrawalBatchConfirm().with_body_params(coinType=BaseConfig.CoinType,
                                                                   businessNo=BaseConfig.CoinType + business_no(),
                                                                   batchId=inputs,
                                                                   result="0")
        response = api.invoke()
        assert (response.get_response_attr("code") == expectedCode["code"])


