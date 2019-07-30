# encoding: utf-8

from core import validator
from core.utils.kv_utils import EasyKVObject

"""

1. Test Suite Level Result
2. Test Case Level Result
"""


class TestCaseResult(EasyKVObject):

    def __init__(self):
        self.status = "pass"


class TestStepResult(EasyKVObject):

    def __init__(self):
        pass


class TestSuiteResult(EasyKVObject):

    def __init__(self):
        pass


class VerificationResult(EasyKVObject):
    def __init__(self, desc, result, msg=None):
        self.desc = desc
        self.result = result
        self.msg = msg


class SimpleTestResultCollector(EasyKVObject):

    def __init__(self):
        self.validation_result = list()
        self.tc_result = "pass"
        self.response_result = {}

    def validate(self, checked_value, expr):
        desc = checked_value + " " + expr
        validate_result = validator.validate(checked_value, expr)
        if validate_result[0] == "failed":
            self.tc_result = "failed"
        self.validation_result.append(VerificationResult(desc, validate_result[0], desc))

    def add_response(self, service, response):
        self.response_result[service] = response

    def get_tc_result(self):
        return self.tc_result

    def get_tc_detail_result(self):
        return self.tc_result, self.validation_result

    def generate_report(self):
        for result in self.validation_result:
            print("{} : {} , msg: {} ".format(result.result, result.desc, result.msg))
