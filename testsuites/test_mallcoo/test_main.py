import allure
import pytest

from api.demo import mallcoo as MallcooAPI
from .mallcoo_base_config import MData


@allure.epic("mallcoo测试demo")
class TestMallCoo:

    # 使用fixture的函数不能在@pytest.mark.parametrize中作为参数使用，只能在函数后当做参数
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






