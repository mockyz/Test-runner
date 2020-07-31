
class MallcooBaseConfig:

    def Login_Data_Case(self):
        Login_Data_Case = {"mallid": 10296, "mobile": "18576706077", "pwd": "123456hu"}
        return Login_Data_Case

    def Select_Data_Case(self,token):
        # TODO：业务逻辑相关的放到case里面去处理，数据只返回数据
        print('ppppp:'+token)
        Select_Data_Case = {'mallid': 10296, 'pageIndex': 2, 'pageSize': 5, "Header": {"Token": token+',15284'}}
        return Select_Data_Case
# 类要初始化、这个是单例模式的一种
MData =  MallcooBaseConfig()

