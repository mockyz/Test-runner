# encoding: utf-8
from core.client import HttpClient


class HttpBinGet(HttpClient):
    req_url = "/get"
    domain = "domain"
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    req_body = {}  ## make sure the some variables with default values
    query_params = []
    method = "GET"


class HttpBinPOST(HttpClient):
    req_url = "/post"
    domain = "domain"
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    req_body = {}  ## make sure the some variables with default values
    query_params = []
    method = "POST"


class HttpBinStatusGet(HttpClient):
    req_url = "/status/{codes}"
    domain = "domain"
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    req_body = {}  ## make sure the some variables with default values
    query_params = []
    method = "GET"
