# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     LoginTestSuite
   Description :
   Author :        patrick
   date：          2019/7/12
-------------------------------------------------
   Change Activity:
                   2019/7/12:
-------------------------------------------------
"""
import allure
import pytest

from api.candybox.candybox_api import Login

__author__ = 'patrick'

error_input = {
    "wrong-password": {
        "nationalCode": "+86",
        "mobile": "18801096079",
        "password": "213241"
    },
    "wrong-phone":
        {
            "nationalCode": "+86",
            "mobile": "18801ds079",
            "password": "11111111"
        }
}

test_cases = ["wrong-password", "wrong-phone"]

## test_cases

@allure.epic("candybox test cases")
class TestCandyBoxLogin:

    @allure.feature("candybox login failed without geetest ")
    def test_candybox_login_wo_geetest(self):
        input_params = {
            "nationalCode": "+86",
            "mobile": "18801096079",
            "password": "11111111"
        }
        result = Login(params=input_params).invoke()
        error_code = result.get_response_data()['code']
        assert error_code == 200099048

    @allure.feature("candybox login failed ")
    @pytest.mark.parametrize("test_case", test_cases)
    def test_candybox_login_failed(self, test_case):
        result = Login(params=error_input[test_case]).invoke()
        print(result.get_status_code())
        assert result.get_status_code() == 500
