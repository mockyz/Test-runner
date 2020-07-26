
VTribeAPI_SERVER = "VTribe"
from core.client import HttpClient


class VTribeAPI(HttpClient):
    method = "POST"
    domain = VTribeAPI_SERVER
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
    req_body = {"username":"${#TestUserName#登陆用户名}", "password":"${#TestPWD#登陆密码}"}
#
# {
#         "batchId": "${#TestCase#批次号}",
#         "businessNo": "${#TestSuite#业务流水号}",
#         "coinType": "${#TestCase#coinType}",
#         "result": "${#TestCase#是否出金}"
#     }