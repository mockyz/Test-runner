from core.client import HttpClient
Mallcoo_SERVER = "mallcoo"


class MallcooAPI(HttpClient):
    method = "POST"
    domain = Mallcoo_SERVER
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


class Login(MallcooAPI):
    """
    登陆
    """
    req_url = "/api/passport/user/Login?_type=3"
    req_body = {"MallID": '${#mallid}', "Mobile": "${#mobile}", "Pwd": "${#pwd}", "SNSType": 0,  "VCode": "",
                "LoginType": 1, "OauthID": None, "Keyword": "", "Scene": 4, "GraphicType": 2, "Header": {"Token": None}}


class SlectIntegral(MallcooAPI):
    """
    查询积分明细
    """
    req_url = "/api/user/Bonus/GetBonusHistoryList?_type=3"
    req_body = {"MallID": '${#mallid}', "PageIndex": '${#pageIndex}', "PageSize": '${#pageSize}',
                "Header": {"Token": '${#token},15284'}}


class GetUserPrivilege(MallcooAPI):
    req_url = "/api/user/User/GetUserPrivilege?_type=3"
    req_body = {"MallID": '${#mallid}', "Header": {"Token": '${#token},15284'}}


class GetTuan(MallcooAPI):
    req_url = "/api/tuan/Tuan/List?_type=3"
    req_body = {"MallId": '${#mallid}', "CategoryId": None, "PageIndex": 0, "Count": 10, "QueryCategory": True,
                 "QueryListType": True, "Header": {"Token": None}}

