import allure
import pytest

from testsuites.test_demo.ontrade_base_config import BaseConfig
from testsuites.test_demo.test_base_intergration import TestOntradeBase

BaseConfig.CoinType = "KLAY"
BaseConfig.Address = {"onTrade_noTrans": "0x84cdBa7dbFbB75EF52bDE8fd833e91A7c8a8aAF2",
                      "onTrade_trans": "0x6f6770f1f67f44fb15b335b49581ad6b935d963a",
                      "outTrade_trans": "0x6f6770f1f67f44fb15b335b49581ad6b935d963a",
                      "outTrade_noTrans": "0x84cdBa7dbFbB75EF52bDE8fd833e91A7c8a8aAF2",
                      "error": "0x84cdBa7dbFbB75EF52bDE8fd833e91A7c8a8aAF2AAAA"}


# pytest C:\Users\mock\PycharmProjects\service-runner\testsuites\ontrade\TestKlayOntrade.py   --alluredir=my_allure_results

@allure.epic("Klay 集成测试")
class TestKlayOntrade(TestOntradeBase):

    @allure.feature("创建地址")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName,inputs,expectedCode', BaseConfig.CREATE_ADDRESS_CASES())
    def test_create_account(self, caseName, inputs, expectedCode):
        self.create_account(BaseConfig, inputs, expectedCode)

    @allure.feature("检查地址有效性")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName,inputs,expectedResult', BaseConfig.CHECK_ADDRESS_CASES())
    def test_check_address_valid(self, caseName, inputs, expectedResult):
        self.check_address_valid(BaseConfig, inputs, expectedResult)

    @allure.feature("查询地址余额")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName,inputs,expectedCode', BaseConfig.QUERY_BANLANCE_CASES())
    def test_query_balance(self, caseName, inputs, expectedCode):
        self.query_balance(BaseConfig, inputs, expectedCode)

    @allure.feature("设置归集阈值")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName,inputs,expectedCode', BaseConfig.Set_Collectthreshold())
    def test_set_collection_threshold(self, caseName, inputs, expectedCode):
        self.set_collection_threshold(BaseConfig, inputs, expectedCode)

    @allure.feature("申请出金")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName,inputs,expectedCode', BaseConfig.Apply_For_Withdrawal())
    def test_apply_for_withdraw(self, caseName, inputs, expectedCode):
        self.apply_for_withdraw(BaseConfig, inputs, expectedCode)

    @allure.feature("确认出金")
    @allure.title("{caseName}")
    @pytest.mark.parametrize('caseName,inputs,expectedCode', BaseConfig.With_Drawal_Bacth())
    def test_confirm_withdraw(self, caseName, inputs, expectedCode):
        self.confirm_withdraw(BaseConfig, inputs, expectedCode)
