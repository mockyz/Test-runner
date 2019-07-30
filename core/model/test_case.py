# encoding: utf-8

from core.utils.kv_utils import EasyKVObject


class TestCase(EasyKVObject):
    """
    load test case data, test case data is a dict or json
    """

    def __init__(self, test_case_data):
        self.name = test_case_data["name"]
        self.tc_id = test_case_data["tc_id"]
        self.steps = self.__make_test_steps(test_case_data["steps"])

    @staticmethod
    def __make_test_steps(steps_data):
        test_steps = list()
        for step in steps_data:
            test_steps.append(TestStep(step))
        return test_steps


class TestStep(EasyKVObject):
    def __init__(self, test_step_data):
        self.service = test_step_data.get("service")
        self.params = test_step_data.get("params", {})
        self.precondition = test_step_data.get("precondition", {})
        self.post_action = test_step_data.get("post_action", {})
        self.verification = test_step_data.get("verification", {})
        self.name = test_step_data.get("name",str(self.service))


def load_test_cases_by_json(test_case_json_path):
    raise NotImplementedError("implement load a json test case file")


def load_test_cases_by_yml(test_data_yaml_path):
    raise NotImplementedError("implement load a yml test case files")


def load_test_cases(test_suite_data):
    test_cases = list()
    for test_case in test_suite_data.get("test_cases", list()):
        test_cases.append(TestCase(test_case))
    return test_cases
