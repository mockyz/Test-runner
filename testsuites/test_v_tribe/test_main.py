
import allure
import pytest
import logging
import json
from api.demo import v_tribe as VTribeAPI

@allure.epic("Klay 集成测试")
class Test_v_trieb:


    @allure.feature("创建地址")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName,inputs,expectedCode', [("test_login", {"username":"sang","password":"123"}, "success")])
    def test_login(self, caseName, inputs, expectedCode):
        api = VTribeAPI.Login().with_body_params(username=inputs["username"],password=inputs["password"])
        response = api.invoke()
        assert response
