# encoding: utf-8
from core.client import HttpClient


class ResponseFormatGet(HttpClient):
    req_url = "/json"
    domain = "domain"
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    req_body = {}  ## make sure the some variables with default values
    query_params = []
    method = "GET"


class FreeFormGet(HttpClient):
    req_url = "/cookies/set"
    domain = "domain"
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    req_body = {}  ## make sure the some variables with default values
    query_params = ["freeform"]
    method = "GET"
