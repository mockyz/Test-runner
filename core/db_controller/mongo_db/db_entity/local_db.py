
from core.db_controller.mongo_db.base.db_base import DBBase


class DBTest(DBBase):
    def __init__(self):
        super(DBTest, self).__init__("47.100.0.26", 26890, "mallcoo", 'user', 'hj', '123456')


class DBTestDebug(DBBase):
    def __init__(self):
        super(DBTestDebug, self).__init__("47.100.0.26", 26890, "mallcoo", "user", 'hj', '123456')


if __name__ == '__main__':
    db = DBTest()
    res1 = db.find_one({'mallid': 10296})
    print(res1)
    # res = db.get_state()
    # print(res)
    # mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}
    # if db.insert_one(mydict):
    #     print('插入成功')
    # else:
    #     print('fail')

    # mydict = {"name": "bbb", 'age': '30'}
    # mydict1 = {"name": "ccc", 'age': '32'}
    # mydict2 = {"name": "ddd", 'age': '35'}
    # if db.insert_many([mydict,mydict1,mydict2]):
    #     print('插入成功')
    # else:
    #     print('fail')
    #
    # res = db.find_many({'name': 'test'}, {'url'})
    # for r in res:
    #     print(r)
    # res1 = db.find_one({'name': 'aaa'})
    # print(res1)
    # res2 = db.find_all({}, {'_id': 0})
    # for r2 in res2:
    #     print(r2)
    # a = ['test', 'aaa']
    # res3 = db.find_in('name', a)
    # for r3 in res3:
    #     print(r3)
    # b = [
    #     {'age': '18'},
    #     {'name': 'aaa'}
    # ]
    # res4 = db.find_or(b)
    # for r4 in res4:
    #     print(r4)
    # res5 = db.find_between('age', '30', '40')
    # for r5 in res5:
    #     print(r5)
    # res6 = db.find_more('age', '30')
    # for r6 in res6:
    #     print(r6)
    # res7 = db.find_less('age', '20')
    # for r7 in res7:
    #     print(r7)
    # res8 = db.find_like('name', 't')
    # for r8 in res8:
    #     print(r8)
    # res9 = db.query_limit(2)
    # for r9 in res9:
    #     print(r9)
    # res10 = db.query_count()
    # print(res10)
    # res11 = db.query_skip(1)
    # for r11 in res11:
    #     print(r11)
    # res12 = db.query_sort([('name', -1)])
    # for r12 in res12:
    #     print(r12)
    # res13 = db.delete_one({'name': 'ccc'})
    # res14 = db.delete_many({'age': '30'})
    # 修改一条数据
    # res15 = db.update_one({'name': '123'}, 'name', 'test')
    # 修改多条数据
    # res16 = db.update_many({"name": {"$regex": "^t"}}, 'age', '99')
