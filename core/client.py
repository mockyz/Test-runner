# encoding: utf-8
import json

import logging
import requests
from requests import Response

from core.environment import TEST_ENV
from core.exceptions import ClientException
from core.utils.extractor import data_extractor
from core.utils.kv_utils import EasyKVObject, kv_util, KVUtil

class Client:

    def __init__(self, env=TEST_ENV):
        # if self.params is not None:
        #     self.params.update(params)
        self.env = env

    def invoke(self, params=None):
        """
        what ever
        :return: ClientResponse
        """
        raise NotImplementedError("abstract class, need an implementation")

    def __call__(self, *args, **kwargs):
        print("client should a callable object or with a invoke method")
        return self.invoke()


http_methods = {

    "get": requests.get,
    "post": requests.post,
    "delete": requests.delete,
    "put": requests.put,
    "option": requests.options
}


class HttpClient(Client):
    req_url = ""
    domain = ""
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    req_body = {}
    query_params = []
    params = {}
    method = "post"

    def __init__(self, env=TEST_ENV):
        super().__init__(env)

    def invoke(self, params=None):
        """
        todo: add parameters to this
        :return:
        """
        if params is not None:
            self.params.update(params)
        if self.params is None:
            self.params = {}
        real_req_url = self.__build_request_url()
        self.__build_header()
        self.build_body()
        http_method = http_methods.get(self.method.lower(), requests.get)
        # todo: handler json and form-data
        self.req_url = real_req_url

        # print(json.dumps(self.req_body))
        logging.info("--------------====----------------")
        logging.info(json.dumps(self.req_body))
        logging.info("--------------====----------------")
        response = http_method(url=self.req_url, headers=self.headers, json=self.req_body, verify=False)
        # print(self)
        print(response.content)
        logging.info("--------------====----------------")
        logging.info(response.content)
        logging.info("--------------====----------------")
        return make_client_response(response)

    def __build_request_url(self):
        if self.env.get_config_by_key(self.domain) is None:
            raise ClientException("domain name should be set in environment or config file")
        else:
            url = self.env.get_config_by_key(self.domain)

        real_req_url = url + self.__make_request_path() + self.__make_query_url()
        return real_req_url

    def __build_header(self):
        if self.params.get("headers", "") != "":
            for h_name, h_value in self.params.get("headers").items():
                self.headers.update({h_name: h_value})

    def __make_request_path(self):
        if self.params is None:
            return self.req_url
        if len(self.params) > 0:
            self.req_url = self.req_url.format(**self.params)
        return self.req_url

    def build_body(self):
        for param_name, param_value in self.params.items():
            kv_util.set_value(self.req_body, param_name, param_value)

    def __make_query_url(self):
        query_url = ""
        if len(self.query_params) > 0:
            query_url = query_url + "?"
        # query_temp ="%s=%s&"
        for query_param in self.query_params:
            if self.params.get(query_param, "") != "":
                query_url = query_url + str(query_param) + "=" + str(self.params.get(query_param, "")) + "&"
        return query_url

    def with_body_param(self, path, value):
        KVUtil.set_value(self.req_body, path, value)
        return self

    def with_body_params(self, **kwargs):
        for key, value in kwargs.items():
            KVUtil.set_value(self.req_body, key, value)
        return self

    def with_header_param(self, path, value):
        KVUtil.set_value(self.headers, path, value)
        return self

    def with_path_param(self, **kwargs):
        for key, value in kwargs.items():
            KVUtil.set_value(self.params, key, value)
        return self

    def with_query_param(self, query_name, query_value):
        if self.params is None:
            self.params = {}
        self.params[query_name] = query_value
        return self

    def __str__(self):
        temp = "req_url:" + self.req_url + "\n"
        temp = temp + "domain:" + self.domain + "\n"
        temp = temp + "headers" + str(self.headers) + "\n"
        temp = temp + "req_params:" + str(self.req_body) + "\n"
        temp = temp + "query_params:" + str(self.query_params) + "\n"
        temp = temp + "method:" + self.method + "\n"
        return temp


class ClientResponse(EasyKVObject):

    def __init__(self, response):
        self.response = response
        self.code = self.get_status_code()
        self.data = self.get_response_data()

    @staticmethod
    def error_client_response():
        return ClientResponse(response={"code": "500"})

    # todo: not completed
    def get_status_code(self):
        if isinstance(self.response, Response):
            return self.response.status_code

        if isinstance(self.response, dict):
            return self.response.get("code", "500")

    # todo: not completed
    def get_response_data(self):

        if isinstance(self.response, Response):
            if self.response.text != "":
                return self.response.json()
            else:
                return ""
        else:
            return self.response

    def get_response_attr(self, key, source="content"):
        """

        :param key:
        :param source: content for response body, header, cookies
        :return:
        """
        if source.lower() == "content" or source.lower() == "body":
            return data_extractor.get_value_by_exp(self.data, key)
        elif source.upper() == "header":
            if isinstance(self.response, Response):
                headers = self.response.headers
                for header_key, header_value in headers.items():
                    if header_key.upper() == key.upper():
                        return header_value
        elif source.upper() == "cookie".upper():
            if isinstance(self.response, Response):
                cookies = self.response.cookies
                for cookie_key, cookie_value in cookies:
                    if cookie_key == key:
                        return cookie_value
        else:
            return self.__dict__.get(key, "")


def make_client_response(resp, resp_type="http"):
    try:
        return ClientResponse(resp)
    except:
        return ClientResponse.error_client_response()
