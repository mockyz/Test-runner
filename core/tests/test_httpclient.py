# encoding: utf-8
import requests

from api.httpbin.schema import HttpBinPOST, HttpBinStatusGet
from core.client import HttpClient
from core.environment import TEST_ENV


class HttpBinGet(HttpClient):
    req_url = "/get"
    domain = "domain"
    headers = {
        "accept": "application/json",
        "content": "application/json"
    }
    req_body = {}  ## make sure the some variables with default values
    query_params = []
    method = "GET"


class TestHttpClient():
    def test_invoker(self):
        params = {"query1": "v2"}
        client = HttpBinGet(params=params, env=TEST_ENV)
        response = client.invoke()
        print(response)

    def test_http_post(self):
        params = {"query1": "v2"}
        client = HttpBinPOST(params=params, env=TEST_ENV)
        response = client()
        print(response.code)
        print(response.data)

    def test_http_post(self):
        params = {"codes": "200"}
        client = HttpBinStatusGet(params=params, env=TEST_ENV)
        response = client()
        print(response.code)
        print(response.data)

    def test_http_bin(self):
        params = {}
        response = requests.post("http://httpbin.org/post",
                                 json=params, headers={"content-type": "application/json"})
        print(response)

    def test_request_url(self):
        req_url = "/status/{codes}"
        params = {"codes": "200"}
        print(req_url.format(**params))

