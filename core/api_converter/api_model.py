# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     api_model
   Description :
   Author :        patrick
   date：          2019/7/11
-------------------------------------------------
   Change Activity:
                   2019/7/11:
-------------------------------------------------
"""
from abc import abstractmethod
from string import Template

from core.api_converter import runner_api_template

__author__ = 'patrick'


class ApiModel:

    def __init__(self, tc=None):
        self.req_url = ""
        self.method = ""
        self.req_body = ""
        self.response_body = ""
        self.name = ""
        self.headers = {}
        for k, v in tc.items():
            setattr(self, k, v)


class BaseApiConverter:

    def __init__(self):
        self.api_context_data = []

    @abstractmethod
    def parse(self, target_file):
        """
        add to api_context_data
        :param target_file:
        :return: self.api_context_data, list of ApiModel
        """
        pass

    def generate_api_testcode(self, test_case):
        self.parse(test_case)
        template_string = runner_api_template
        api_template = Template(template_string)
        for context in self.api_context_data:
            sample_code = api_template.substitute(context)
            print(sample_code)




# def test_collection_to_api_model(test_collection):
#     api = ApiModel(test_collection)
#     return api


# tc = {
#     "req_url": "testing",
#     "method": "post",
#     "req_body": "body",
#     "response_body": "res_body",
#     "name": "name",
#     "headers": {}
# }
#
# api = test_collection_to_api_model(tc)
# print(api)

