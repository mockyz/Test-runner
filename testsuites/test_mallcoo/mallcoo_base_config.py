from testsuites.test_mallcoo.test_main import Test_mallcoo


class MallcooBaseConfig:
    def Get_Token(self):
        token = Test_mallcoo.test_login
        return token

    def Login_Data_Case(self):
        Login_Data_Case = {"mallid": 10296, "mobile": "18576706077", "pwd": "123456hu"}
        return Login_Data_Case

    def Select_Data_Case(self):
        token = self.Get_Token()
        Select_Data_Case = {'mallid': 10296, 'pageIndex': 2, 'pageSize': 5, 'token': token}
        return Select_Data_Case
