from core.db_controller.mongo_db.base.db_base import DBBase

class DBTest(DBBase):
    def __init__(self):
        super(DBTest, self).__init__("47.100.0.26", 27017, "mallcoo_test", 'user')

class MallcooBaseConfig:

    def Login_Data_Case(self):
        db = DBTest()
        Login_Data_Case = db.find_one({'mallid': 10296}, {'_id': 0})
        # Login_Data_Case = {"mallid": 10296, "mobile": "18576706077", "pwd": "123456hu"}
        return Login_Data_Case

    def Select_Data_Case(self, token):
        # TODO：业务逻辑相关的放到case里面去处理，数据只返回数据
        print('ppppp:'+token)
        Select_Data_Case = {'mallid': 10296, 'pageIndex': 2, 'pageSize': 5, "Header": {"Token": token+',15284'}}
        return Select_Data_Case
# 类要初始化、这个是单例模式的一种
MData = MallcooBaseConfig()

if __name__ == '__main__':
    db = DBTest()
    re = db.find_all({}, {"_id": 0})
    for user in re:
        print(user)
