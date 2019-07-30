# encoding: utf-8
import allure

from api.httpbin.schema import HttpBinGet, HttpBinPOST
from core.tc_executor import IntegrationExecutor

httpbin_testcases = {
    "login": {
        "serviceName": "",
        "params": "",
        "post_action": ""
    },
    "test_cases": [{
        "name": "tc description",
        "tc_id": "testCaseId",
        "steps": [
            {
                "name": "http get api",
                "precondition": {},
                "service": HttpBinGet,
                "params": {},
                "post_action": {"url": "url", "args": "args"},
                "verification": {"url": "is_equal_to http://httpbin.org"}
            },
            {
                "name": "http post api",
                "precondition": {},
                "service": HttpBinPOST,
                "params": {},
                "post_action": {},
                "verification": {"url": "is_equal_to http://httpbin.org"}
            }
        ]
    }]
}


httpbinget_testcases = {
    "test_cases": [{
        "name": "getapi-tc-1",
        "tc_id": "tc-get-1",
        "steps": [
            {
                "name": "http get api",
                "precondition": {},
                "service": HttpBinGet,
                "params": {},
                "verification": {"url": "is_equal_to http://httpbin.org"}
            }
        ]}
    ,{
        "name": "getapi-tc-21",
        "tc_id": "tc-get-2",
        "steps": [
            {
                "name": "http get api",
                "precondition": {},
                "service": HttpBinGet,
                "params": {},
                "verification": {"headers.Accept": "is_equal_to application/json1"}
            }
        ]}

    ]
}



@allure.epic("testing http bin test cases")
class TestHttpBinTestCase:

    @allure.feature("testing http bin get")
    def test_httpbin_get(self):
        runner = IntegrationExecutor(httpbinget_testcases)
        result = runner.run()
        assert result.get_tc_result() == "pass"

    @allure.feature("testing http bin get/post")
    def test_httpbin_tc(self):
        runner = IntegrationExecutor(httpbin_testcases)
        result = runner.run()
        assert result.get_tc_result() == "pass"
