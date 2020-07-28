import allure
import pytest
import logging
import json

from api.demo import mallcoo as MallcooAPI


@allure.epic("mallcoo测试demo")
class Test_mallcoo:
    login_data = {"mallid": 10296, "mobile": "18576706077", "pwd": "123456hu"}
    token = ''

    @allure.feature("mallcoo测试demo-login")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName,inputs, expectedCode', [("test_login", login_data, "success")])
    def test_login(self, caseName, inputs, expectedCode):
        api = MallcooAPI.Login().with_body_params(MallID=inputs["mallid"], Mobile=inputs["mobile"], Pwd=inputs['pwd'])
        response = api.invoke()
        assert response.get_status_code() == 200
        assert response.get_response_attr('m') == 1
        # response.get_response_attr('d')是dict类型，不能用for循环
        assert response.get_response_attr('d')['MallID'] == 10296
        print(response.get_response_attr('d')['Token'])
        global token
        token = response.get_response_attr('d')['Token']

    select_data = {'mallid': 10296, 'pageIndex': 2, 'pageSize': 5, 'token': token}

    @allure.feature("mallcoo测试demo-select")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName,inputs, expectedCode', [("test_selectIntefral", select_data, "success")])
    def test_slectIntegral(self, caseName,inputs, expectedCode):
        api = MallcooAPI.SlectIntegral().with_body_params(MallID=inputs["mallid"], PageIndex=inputs["pageIndex"],
                                                          PageSize=inputs['pageSize'], Token=inputs['token'])
        response = api.invoke()
        assert response.get_status_code() == 200




