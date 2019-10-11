# encoding: utf-8
import allure

from api.httpbin.response_format import ResponseFormatGet, FreeFormGet
from core.tc_executor import IntegrationExecutor

context_demo_cases = {
    "test_cases": [{
        "name": "tc description",
        "tc_id": "testCaseId",
        "steps": [
            {
                "name": "call json api to get author name",
                "precondition": {},
                "service": ResponseFormatGet,
                "params": {

                },
                "post_action": {"author": "slideshow.author"},
            },
            {
                "name": "call set cookie to verify the result",
                "precondition": {},
                "service": FreeFormGet,
                "params": {"freeform": "{{author | replace(' ','space')}}"},
                "post_action": {},
                "verification": {"cookies.freeform": "is_equal_to {{author | replace(' ','space')}}"}
            }
        ]
    }]
}


@allure.epic("testing http bin freeform test cases")
class TestFreeFormCase:

    @allure.feature("测试HTTP BIN 接口")
    def test_httpbin_freeform(self):
        runner = IntegrationExecutor(context_demo_cases)
        result = runner.run()
        assert result.get_tc_result() == "pass"
