import allure
import pytest

from api.demo import mallcoo as MallcooAPI
from  .mallcoo_base_config import MData


@allure.epic("mallcoo测试demo")
class TestMallCoo:


    @pytest.fixture()
    def login(self):
        inputs = MData.Login_Data_Case()
        api = MallcooAPI.Login().with_body_params(MallID=inputs["mallid"], Mobile=inputs["mobile"], Pwd=inputs['pwd'])
        response = api.invoke()
        assert response.get_status_code() == 200
        assert response.get_response_attr('m') == 1
        assert response.get_response_attr('d')['MallID'] == 10296
        token = response.get_response_attr('d')['Token']
        return token

    @allure.feature("mallcoo测试demo-select")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName, expectedCode', [("selectHistory", "success")])
    def test_history(self, caseName, expectedCode, login):
        inputs = MData.Select_Data_Case(login)
        api = MallcooAPI.SlectIntegral().with_body_params(MallID=inputs["mallid"], PageIndex=inputs["pageIndex"],
                                                          PageSize=inputs['pageSize'], Header=inputs["Header"])
        response = api.invoke()
        assert response.get_status_code() == 200
        assert response.get_response_attr('m') == 1






