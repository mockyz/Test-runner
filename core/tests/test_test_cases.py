# encoding: utf-8
from core.model.test_case import load_test_cases


class TestTestCases:
    def test_load_test_cases(self):
        test_cases_data = {
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
                        "step": {
                            "name": "",
                            "precondition": {},
                            "service": "",
                            "params": "",
                            "post_action": {},
                            "verification": {}
                        }
                    },
                    {
                        "step": {
                            "name": "",
                            "precondition": {},
                            "service": "",
                            "params": "",
                            "post_action": {},
                            "verification": {}
                        }
                    }
                ]
            }]
        }

        result = load_test_cases(test_cases_data)
        print(result[0].to_json())
        print(result[0].to_dict())
        print(result[0].to_json_with_module())
