# # -*- coding: utf-8 -*-
# import copy
# import json
#
# import requests
#
# available_request_methods = {"get": requests.get, "post": requests.post}
#
#
# class ExternalAPI(object):
#     api_description = {
#         'url': '',
#         'request_body': {},
#         'method': 'post',
#         'headers': {'content-type': 'application/json'},
#         'query_params': {},
#         'data': {}
#     }
#
#     def __init__(self, params={}):
#         self.params = copy.deepcopy(params)
#         self.url = self.api_description.get('url', '')
#         self.request_body = self.api_description.get('request_body', {})
#         self.method = self.api_description.get('method', 'post')
#         self.response = None
#         self.query_params = self.api_description.get('query_params', {})
#         self.headers = self.api_description.get('headers', {'content-type': 'application/json'})
#         self.data = self.api_description.get('data', {})
#         self.case_step_content = {}
#
#     def build_header(self):
#         if self.api_description.get('headers'):
#             for item in self.api_description['headers']:
#                 self.headers[item] = self.api_description['headers'][item]
#
#     def build_request_body(self):
#         """
#         组合params到request body
#         :return:
#         """
#         pass
#
#     def build_request_params(self):
#         pass
#
#     def request_url(self):
#         pass
#
#     def build_request_data(self):
#         """
#         for Form Data Request,
#         将params 转化为form data
#         :return:
#         """
#         pass
#
#     def post_handler(self):
#         """
#         if response is not json, mock it to json using FakeResponse
#         :return:
#         """
#         return self.response
#
#     def request_method(self):
#         return available_request_methods.get(self.method)
#
#     def process_authorization(self):
#         pass
#
#     def api_call(self):
#         self.request_url()
#         self.build_header()
#         self.build_request_params()
#         self.build_request_data()
#         self.build_request_body()
#         self.build_case_step_content()
#
#         request_data = json.dumps(self.request_body) if len(self.data) == 0 else self.data
#         print("request url:", self.url)
#         print('request body:', json.dumps(self.request_body, ensure_ascii=False))
#         self.response = self.request_method()(url=self.url,
#                                               params=self.query_params,
#                                               data=request_data,
#                                               headers=self.headers)
#         print("response:", self.response.content)
#         return self.post_handler()
#
#     def build_case_step_content(self):
#         self.case_step_content['step_description'] = "invoke api " + self.__class__.__name__
#         self.case_step_content['baseUrl'] = self.url
#         self.case_step_content['request_data'] = json.dumps(self.request_body, ensure_ascii=False)
#         self.case_step_content['headers'] = self.headers
#
#
# class SoaClient(ExternalAPI):
#     def build_request_body(self):
#
#         """
#             将params 转化为query parameter
#             Build request params for both query parameters
#             :return:
#         """
#         if self.params:
#             for k in self.params:
#                 self.request_body['args'][k] = self.params[k]
#         return self.request_body
#
#
# class MQPublisher(ExternalAPI):
#     def build_request_body(self):
#         payload = json.loads(self.request_body['payload']) if type(self.request_body['payload']) == str else \
#             self.request_body['payload']
#         if self.params:
#             for k in self.params:
#                 payload[k] = self.params[k]
#         self.request_body['payload'] = json.dumps(payload, ensure_ascii=False)
