# encoding: utf-8
from collections import ChainMap

from core import get_logger
from core.client import Client
from core.environment import TEST_ENV
from core.model import test_case
from core.model.test_result import SimpleTestResultCollector
from core.report.reporter import PlainReporter
from core.utils import kv_util
from core.utils.template_render import render_to_dict


class IntegrationExecutor:

    def __init__(self, test_cases, env=TEST_ENV):
        self.logger = get_logger()
        self.context = ChainMap()
        self.reporter = PlainReporter()
        self.test_cases = test_case.load_test_cases(test_cases)
        ## todo: add to test result when running test
        self.test_result_collector = SimpleTestResultCollector()
        self.env = env

    def _run_step(self, test_step):

        service_type = test_step.service
        if issubclass(service_type, Client):
            service = service_type(test_step.params, env=self.env)
            self.logger.msg("request params: {}".format(test_step.params))
            client_response = service.invoke()
            self.logger.msg(client_response.to_json())
            self.test_result_collector.add_response(test_step.name, client_response)
            return client_response

    def _process_pre_condition(self, test_step):
        if self.context.get("headers", "") != "":
            for h_name, h_value in self.context.get("headers").items():
                test_step.params.get("header", {}).update({h_name: h_value})
        test_step.params = render_to_dict(test_step.params, context=self.context)
        test_step.verification = render_to_dict(test_step.verification, context=self.context)

    def __process_post_action(self, post_action, last_result):
        """
        todo: enough for most cases, need to add extract header or cookie like
        :param post_action:
        :param last_result:
        :return:
        """
        for key, value in post_action.items():
            self.context[key] = kv_util.get_value(last_result.data, value)

    def run(self):
        self._run_global_step()
        for test_case in self.test_cases:
            for step in test_case.steps:
                self._process_pre_condition(step)
                result = self._run_step(test_step=step)
                self.__process_post_action(step.post_action, last_result=result)
                self._process_verification(test_step=step, response=result)

        self.test_result_collector.generate_report()
        return self.test_result_collector

    def _process_verification(self, test_step, response):
        verifications = test_step.verification
        for v_key, v_value in verifications.items():
            self.test_result_collector.validate(kv_util.get_value(response.data, v_key), v_value)

    def _run_global_step(self):
        """
        run global step for login or other pre-condition
        :return:
        """
        print("running steps........")
