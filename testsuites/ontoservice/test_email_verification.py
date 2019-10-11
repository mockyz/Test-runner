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

from api.ontoservice.onto_service_api import SendEmailVerificationCode
from api.ontoservice.onto_service_api import VerifyEmailCode
from core.utils.assertpy import assert_that
from core.utils.dbwrapper import DBWrapper

__author__ = 'patrick'


@allure.epic("email verification")
class TestOntoServiceVerification:

    @allure.feature("send email verification failed")
    def test_send_email_code_invalid_device_code(self):
        send_email = SendEmailVerificationCode()
        response = send_email.invoke({})
        assert_that(response.get_response_attr("Error")).is_equal_to(63003)
        assert_that(response.get_response_attr("Desc")).is_equal_to("FAIL, verify devicecode fail.")

    @allure.feature("send email verification successfully")
    def test_send_email_code_successfully(self):

        # data = "did:ont:ALaRqCkXSWaHMDc5sLEEMVMWqCNDFi5eRZ"
        # devicecode = "device123"
        send_email = SendEmailVerificationCode()
        send_email.with_body_param("OwnerOntId", "did:ont:ALaRqCkXSWaHMDc5sLEEMVMWqCNDFi5eRZ").with_body_param("DeviceCode", "device123").with_body_param("Email", "huangjiahuan@onchain.com")
        response = send_email.invoke()
        assert_that(response.get_response_attr("Result")).is_equal_to(True)
        assert_that(response.get_response_attr("Desc")).is_equal_to("SUCCESS")

    @allure.feature("email code verify  failed")
    def test_code_verify_default_null(self):
        verify_code = VerifyEmailCode()
        verify_code.with_query_param("email", "").with_query_param("code", "")
        response = verify_code.invoke()
        # assert_that(response.get_response_attr("Error")).is_equal_to(61001)
        assert_that(response.get_response_attr("Result")).is_equal_to(False)

    @allure.feature("email code verify  failed2")
    def test_code_verify_param_space(self):
        verify_code = VerifyEmailCode()
        verify_code.with_query_param("email", " ").with_query_param("code", " ")
        response = verify_code.invoke()
        assert_that(response.get_response_attr("Error")).is_equal_to(61001)
        assert_that(response.get_response_attr("Result")).is_equal_to(False)
        assert_that(response.get_response_attr("Desc")).is_equal_to("must be a well-formed email address")

    @allure.feature("email code verify  failed3")
    def test_code_verify_param_error(self):
        verify_code = VerifyEmailCode()
        verify_code.with_query_param("email", "123rrtgmm").with_query_param("code", "122")
        response = verify_code.invoke()
        assert_that(response.get_response_attr("Error")).is_equal_to(61001)
        assert_that(response.get_response_attr("Result")).is_equal_to(False)
        assert_that(response.get_response_attr("Desc")).is_equal_to("must be a well-formed email address")

    @allure.feature("email code verify  failed4")
    def test_code_verify_code_error(self):
        verify_code = VerifyEmailCode()
        verify_code.with_query_param("email", "huangjiahuan@onchain.com").with_query_param("code", "123123")
        response = verify_code.invoke()
        assert_that(response.get_response_attr("Error")).is_equal_to(61003)
        assert_that(response.get_response_attr("Desc")).is_equal_to("FAIL, not found.")
        assert_that(response.get_response_attr("Result")).is_equal_to(False)

    @allure.feature("email code verify  success")
    def test_code_verify_code_success(self):
        verify_code = VerifyEmailCode()
        db = DBWrapper.get("ontpass")
        res = DBWrapper.execute(db, "select * from tbl_ont_email")
        verify_code.with_query_param("email", "huangjiahuan@onchain.com").with_query_param("code", res[0]["Code"])
        response = verify_code.invoke()
        assert_that(response.get_response_attr("Desc")).is_equal_to("SUCCESS")
        assert_that(response.get_response_attr("Result")).is_equal_to(True)








