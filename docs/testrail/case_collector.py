# # -*- coding: utf-8 -*-
# import json
#
# import base
# import requests
# import yaml
# from base.env import target_env, JENKINS
# from base.testrail import *
# from base.utils import date_util
#
#
# class CaseCollector(object):
#     """
#     Case Collector, #todo need refactor
#     """
#     def __init__(self, project_name=None, module_name=None, method_name=None):
#         """
#         1. project_name: project_name
#         2. module_name: default Master, mapping to suite_name in test rail
#         3.
#         :param project_name:
#         :param module_name:
#         :param method_name:
#         """
#         self.project_name = project_name if project_name else 'NAPOS_SHOP_API'
#         self.suite_name = module_name if module_name else 'Master'
#         self.section_name = method_name
#         self.title = None
#         # todo it is content/expected
#         self.case_steps = []
#         self.case_data = {}
#         self.result_steps = []
#         self.result_data = {}
#         self.run_data = {}
#         self.test_result_status = '1'
#         self.run_name = base.testrail.run_name
#
#     def collect(self):
#
#         if target_env.client_name == JENKINS:
#             if len(self.result_steps) == 0:
#                 self.test_result_status = 5
#             self.collect_case()
#             self.collect_test_result()
#
#     def collect_case(self):
#         """
#         collect test result info and test case info
#         :return:
#         """
#         try:
#             self._build_test_rail_case_data()
#             if self.case_data['title']:
#                 return requests.post(TEST_RAIL_URL_CASE,
#                                      headers={"content-type": "application/json"},
#                                      data=json.dumps(self.case_data))
#
#         except Exception:
#             print("the test bridge server is not available")
#
#     def collect_test_result(self):
#         """
#         collect test result data
#         :return:
#         """
#         self._build_test_rail_result_data()
#         if self.case_data['title']:
#             return self._test_rail_request(TEST_RAIL_URL_RESULT, self.result_data)
#
#     def start_test_run(self):
#         if base.testrail.new_run_flag and target_env.client_name == JENKINS:
#             base.testrail.run_name = "_".join([self.project_name,
#                                                self.suite_name,
#                                                date_util.get_format_datetime()])
#             self.run_name = base.testrail.run_name
#             self._build_run_data()
#             base.testrail.new_run_flag = False
#             return self._test_rail_request(TEST_RAIL_URL_RUN, self.run_data)
#
#     def _test_rail_request(self, url, data):
#         """
#         post to invoke test rail middleware apis
#         :param url:
#         :param data:
#         :return:
#         """
#         try:
#             return requests.post(url, headers={"content-type": "application/json"}, data=json.dumps(data))
#         except Exception:
#             print("the test bridge server is not available")
#
#     def _build_test_rail_result_data(self):
#         """
#         build test result data
#         :return:
#         """
#         self.result_data['runName'] = self.run_name
#         self.result_data['projectname'] = self.project_name
#         self.result_data['caseInfo'] = self.case_data
#         self.result_data['resultSteps'] = self.result_steps
#         self.result_data['status'] = self.test_result_status
#
#     def _build_run_data(self):
#         """
#         build run data
#         :return:
#         """
#         self.run_data['name'] = self.run_name
#         self.run_data['project_name'] = self.project_name
#         self.run_data['suite_name'] = self.suite_name
#
#     def _build_test_rail_case_data(self):
#         """
#         build test result data
#         :return:
#         """
#         self.case_data['project_name'] = self.project_name
#         self.case_data['suite_name'] = self.suite_name
#         self.case_data['section_name'] = self.section_name
#         self.case_data['title'] = self.title
#         self.case_data['caseSteps'] = self.case_steps
#
#     def add_case_step(self, case_step):
#         """
#         add test case step
#         :param case_step:
#         :return:
#         """
#         self.case_steps.append(case_step.to_dict())
#         return self
#
#     def add_result_step(self, result_step):
#         """
#         add test result step
#         :param result_step:
#         :return:
#         """
#         if result_step.status == '5':
#             self.test_result_status = '5'
#         self.result_steps.append(result_step.to_dict())
#         return self
#
#
# class CaseStep(object):
#     """
#     Case Step description
#     """
#
#     def __init__(self, api_requests=None, expected=None):
#         self.content = yaml.dump(api_requests, default_flow_style=False,
#                                  allow_unicode=True) if api_requests else api_requests
#         self.expected = yaml.dump(expected, default_flow_style=False, allow_unicode=True) if expected else expected
#
#     def to_dict(self):
#         return {"content": self.content, "expected": self.expected}
#
#     def __repr__(self):
#         return self.to_dict()
#
#
# class TestResultStep(object):
#     """
#     Test Result Step: for record test step and result
#     public interface TestRailResult {
#     String PASSED = "1";
#     String FAILED = "5";
#     String BLOCKED = "2";
#     String UNTESTED = "3";
#     String RRETESTED = "4";
#     String PASSED_STRING = "Passed";
#     String FAILED_STING = "Failed";
#     String BLOCKED_STRING = "Blocked";
#     String UNTESTED_STRING = "Untested";
#     String RRETESTED_STRING = "Retest";
#     }
#     """
#
#     def __init__(self, api_requests=None, response_content=None, expected=None, status=None):
#         self.content = yaml.dump(api_requests, default_flow_style=False,
#                                  allow_unicode=True) if api_requests else None
#         # self.response =  yaml.dump(response.json(), default_flow_style=False,
#         #                          allow_unicode=True) if response else None
#         self.expected = yaml.dump(expected,
#                                   default_flow_style=False,
#                                   allow_unicode=True) if expected else None
#
#         self.actual = yaml.dump(response_content, default_flow_style=False,
#                                 allow_unicode=True) if response_content else None
#         self.status = "1" if status else "5"
#
#     def to_dict(self):
#         return {"content": self.content,
#                 "expected": self.expected,
#                 "actual": self.actual,
#                 "status": self.status}
#
#     def __repr__(self):
#         return self.to_dict()
#
# # if __name__ == '__main__':
# #     CaseCollector(project_name="NAPOS_SHOP_API").start_test_run()
