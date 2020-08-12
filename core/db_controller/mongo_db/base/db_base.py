from .mongodb_operation import BaseHandle
from pymongo import MongoClient

class DBBase(object):

    def __init__(self, host, port, database, collection, username, password):
        self.conn = MongoClient(host, port)
        self.db = self.conn[database]
        self.db.authenticate(username, password, mechanism='SCRAM-SHA-1')
        self.collection = self.db[collection]
        self.query = self.collection.find()

    def get_state(self):
        return self.conn is not None and self.collection is not None

    def insert_one(self, data):
        res = BaseHandle.insert_one(self.collection, data)
        return res

    def insert_many(self, data_list):
        res = BaseHandle.insert_many(self.collection, data_list)
        return res

    def find_one(self, data, data_field={}):
        res = BaseHandle.find_one(self.collection, data, data_field)
        return res

    def find_many(self, data, data_field={}):
        """ 有多个键值的话就是 AND 的关系"""
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_all(self, data={}, data_field={}):
        """select * from table"""
        print("-------")
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_in(self, field, item_list, data_field={}):
        """SELECT * FROM inventory WHERE status in ("A", "D")"""
        data = dict()
        data[field] = {"$in": item_list}
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_or(self, data_list, data_field={}):
        """db.inventory.find(
    {"$or": [{"status": "A"}, {"qty": {"$lt": 30}}]})

        SELECT * FROM inventory WHERE status = "A" OR qty < 30
        """
        data = dict()
        data["$or"] = data_list
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_between(self, field, value1, value2, data_field={}):
        """获取俩个值中间的数据"""
        data = dict()
        data[field] = {"$gt": value1, "$lt": value2}
        # data[field] = {"$gte": value1, "$lte": value2} # <>   <= >=
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_more(self, field, value, data_field={}):
        data = dict()
        data[field] = {"$gt": value}
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_less(self, field, value, data_field={}):
        data = dict()
        data[field] = {"$lt": value}
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_like(self, field, value, data_field={}):
        """ where key like "%audio% """
        data = dict()
        data[field] = {'$regex': '.*' + value + '.*'}
        print(data)
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def query_limit(self, num):
        """db.collection.find(<query>).limit(<number>) 获取指定数据"""
        res = self.query.limit(num)
        # res = query.limit(num)
        return res

    def query_count(self):
        res = self.query.count()
        return res

    # 跳过指定条数据
    def query_skip(self, num):
        res = self.query.skip(num)
        return res

    def query_sort(self, data):
        """db.orders.find().sort( { amount: -1 } ) 根据amount 降序排列"""
        res = self.collection.find().sort(data)
        return res

    def delete_one(self, data):
        """ 删除单行数据 如果有多个 则删除第一个"""
        res = BaseHandle.delete_one(self.collection, data)
        return res

    def delete_many(self, data):
        """ 删除查到的多个数据 data 是一个字典 """
        res = BaseHandle.delete_many(self.collection, data)
        return res

    def update_one(self, data_condition, data_set, value):
        """修改一条数据,data_condition为查询条件，data_set为修改字段，value为修改后值"""
        res = BaseHandle.update_one(self.collection, data_condition, data_set, value)
        print('修改成功')
        return res

    def update_many(self, data_condition, data_set, value):
        """修改多条数据,data_condition为查询条件，data_set为修改字段，value为修改后值"""
        res = BaseHandle.update_many(self.collection, data_condition, data_set, value)
        print('修改成功')
        return res
