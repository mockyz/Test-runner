# # -*- coding: utf-8 -*-
#
#
# import json
# import records
# from base.env import target_env
# from jinja2 import Template
# import pymysql
#
# pymysql.install_as_MySQLdb()
#
#
#
# class DBWrapper(object):
#     """
#     Database wrapper for records
#     """
#
#     def __init__(self, db):
#         self.db = db
#
#     @staticmethod
#     def get(db_config):
#         db = records.Database(db_config)
#         return DBWrapper(db)
#
#     def api_call(self, params):
#         if target_env.profile == 'prod':
#             return None
#         if params.get("sql_params"):
#             sql = Template(params["sql"]).render(params["sql_params"])
#         else:
#             sql = params.get('sql')
#         if (sql.upper().find('UPDATE') >= 0 or sql.upper().find('DELETE') >= 0) \
#                 and sql.upper().find('WHERE ') < 0:
#             raise Exception("invalid sql, update/delete sql statement must have where")
#         result = self.db.query(sql)
#         try:
#             return {"result": json.loads(result.export('json'))}
#         except:
#             return {"message": "db operation is executed successfully"}
#
#
