# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     postman_parser
   Description :
   Author :        patrick
   date：          2019/7/11
-------------------------------------------------
   Change Activity:
                   2019/7/11:
-------------------------------------------------
"""
import json
import uuid
from string import Template

from core.api_converter import runner_api_template
from core.api_converter.api_model import ApiModel

__author__ = 'patrick'


# with open('login.json', 'r') as context:
#     lines = context.readlines()
#     print(lines)


class PostManParser:

    def __init__(self):
        self.api_defs = {}
        self.api_context_data = []

    def _load_test_case(self, postman_file):
        with open(postman_file, 'r') as api_collection:
            self.api_defs = json.load(api_collection)

    def parse(self, postman_file):

        self._load_test_case(postman_file)
        api_items = self.api_defs['item']
        # todo: item in item case
        for item in api_items:
            ## todo: handle item in v2.1
            raw_body = item['request'].get('body', {})
            body = raw_body.get("raw", {})
            headers = {}
            for header_item in item['request']['header']:
                headers[header_item['key']] = header_item['value']

            api_def = {'name': item['name'], 'req_url': item['request']['url']['raw'], 'headers': headers,
                       'req_body': body, 'method': item['request']['method']}
            self.api_context_data.append(api_def)

    def generate_api_testcode(self, test_case):
        self.parse(test_case)
        template_string = runner_api_template
        api_template = Template(template_string)
        for context in self.api_context_data:
            sample_code = api_template.substitute(context)
            print(sample_code)


def parse_req_url(req_url):
    """
    parse request url to protocol,host,path,query
    :param req_url:
    :return:
    """
    if req_url.startswith("https:"):
        protocol = "https"
    else:
        protocol = "http"

    url = req_url.replace(protocol + "://", "")

    path_array = url.split("/")
    host = path_array[0]
    paths = path_array[1:-1]
    last_path = path_array[len(path_array) - 1]
    query = []
    if len(last_path.strip()) > 0:
        query_params = last_path.split("?")
        if len(query_params) == 1:
            paths.append(query_params[0].strip())
        else:
            query_params_str = query_params[1]
            query_array = query_params_str.split("&")
            for query_str in query_array:
                query_str_arr = query_str.split("=")
                query_item = {
                    "key": query_str_arr[0],
                    "value": query_str_arr[1]
                }
                query.append(query_item)

    return protocol, host, paths, query


class PostmanLogger:
    POSTMAN_INFO = {"info": {
        "_postman_id": uuid.uuid1(),
        "name": "",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    }}
    POSTMAN_ITEM = {"name": "重置密码时发送手机验证码",
                    "request": {
                        "method": "POST",
                        "header": [
                            {
                                "key": "Content-Type",
                                "value": "{{contentType}}",
                                "type": "text"
                            },
                            {
                                "key": "Secure-Key",
                                "value": "Ioo0sMzj1xOp1nTdOwdta8IJiJobREDaWEYZlBhhBGn6TTwxlxzcwlfuWRO6zFxBVcw4MPWfVyXbTw9okxQD7oh0CJVBKr04AKjUfHJjcgiXB5vbe73NojuQsJ7KSQYBbvAE6lxSctv9BZxo7YNt+Qreyppwnn21xQMUqTawDPw=",
                                "type": "text"
                            },
                            {
                                "key": "Accept",
                                "value": "{{Accept}}",
                                "type": "text"
                            }
                        ],
                        "body": {
                            "mode": "raw",
                            "raw": "{\n    \"data\": \"ueXokQ3v3CRxn7xCHzUOhJr/b0bT8ntpxmenAg2WeQcopWMoUQZbMcq3xsQK2JcKnsJRF4a4mftNUWjhCv+2M2XazP2DYqzUaNqQ/dNmCszAkcn86FN5Ow9wCkoy4G/FVTGzHa11nTvRt5ecqz1mHg==\"\n}"
                        },
                        "url": {
                            "raw": "{{url31}}/web/v1/users/phone/reset-password-verification-code",
                            "host": [
                                "{{url31}}"
                            ],
                            "path": [
                                "web",
                                "v1",
                                "users",
                                "phone",
                                "reset-password-verification-code"
                            ]
                        },
                        "query": [
                            {
                                "key": "phone",
                                "value": "86*17157727684"
                            }
                        ]
                    },
                    "response": []
                    }

    def __init__(self):
        pass

    def log_postman(self):
        pass

    @staticmethod
    def convert_to_postman(test_collections):
        postman_items = []
        for collection in test_collections:
            api = ApiModel(collection)
            postman_api = {
                "name": api.name,
            }
            postman_request = {'body': {
                "mode": "raw",
                "raw": api.req_body
            }, 'method': api.method}
            protocol, host, paths, query = parse_req_url(api.req_url)
            postman_request['url'] = {
                "raw": api.req_url,
                "host": host,
                "paths": paths,
                "query": query
            }
            postman_api['request'] = postman_request
            postman_api['response'] = []  # todo
            postman_items.append(postman_api)
        return postman_items


if __name__ == '__main__':
    PostManParser().generate_api_testcode("wallet service interface.postman_collection.json")
