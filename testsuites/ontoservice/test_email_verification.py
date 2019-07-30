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
import allure

import api.ontoservice.onto_service_api as OntoServiceAPI
from core.utils.assertpy import assert_that

__author__ = 'patrick'


@allure.epic("email verification")
class TestOntoServiceVerification:

    @allure.feature("send email verification failed")
    def test_send_email_code_invalid_device_code(self):
        send_email = OntoServiceAPI.SendEmailVerificationCode()
        response = send_email.invoke({})
        assert_that(response.get_response_attr("Error")).is_equal_to(63003)
        assert_that(response.get_response_attr("Desc")).is_equal_to("FAIL, verify devicecode fail.")

    @allure.feature("send email verification successfully")
    def test_send_email_code_successfully(self):
        pass



