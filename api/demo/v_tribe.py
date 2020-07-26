
VTribeAPI_SERVER = "VTribeAPI"
from core.client import HttpClient


class VTribeAPI(HttpClient):
    method = "POST"
    domain = "http://47.100.0.26:8081"
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    def build_body(self):
        for k, v in self.params.items():
            if self.req_body.get(k) is not None:
                self.req_body[k] = v
            else:
                self.req_body.get('data')[0][k] = v


class Login(VTribeAPI):
    """
    登陆
    username=sang&password=123&
    """
    req_url = "/login"
    req_body = {
        "businessNo": "",
        "data": ""
    }

