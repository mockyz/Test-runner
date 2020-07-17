from db_controller.mongo_db.base.db_base import DBBase


class DBTest(DBBase):
    def __init__(self):
        super(DBTest, self).__init__("127.0.0.1", 27017, "test")


class DBTestDebug(DBBase):
    def __init__(self):
        super(DBTestDebug, self).__init__("127.0.0.1", 27017, "test","test_debug")


if __name__ == '__main__':
    db = DBTestDebug()
    res = db.find_all()
    print(res)
