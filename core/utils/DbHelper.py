# -*- coding: UTF-8 -*-
# !/usr/bin/env

import pymysql
import logging

class DbHelper:
    @staticmethod
    def query_one(sql):
        conn = DbHelper.get_conn()
        cur = conn.cursor()
        try:
            cur.execute(sql)    # 执行sql语句
            return cur.fetchone()
        except Exception as e:
            logging.error(u"数据查询错误%s", e.message)
            raise e
        finally:
            conn.close()  # 关闭连接
        return None

    @staticmethod
    def query_data(sql):
        row = DbHelper.queryOne(sql)
        if row is not None:
            return row[0]
        return None

    @staticmethod
    def query_collection(sql):
        # type: (object) -> object
        conn = DbHelper.get_conn()
        cur = conn.cursor()
        try:
            cur.execute(sql)    # 执行sql语句
            return cur.fetchall()
        except Exception as e:
            logging.error(u"数据查询错误%s",e.message)
            raise e
        finally:
            conn.close()  # 关闭连接
        return []

    @staticmethod
    def execute_sql(sql):
        conn = DbHelper.get_conn()
        cur = conn.cursor()
        try:
            cur.execute(sql)    # 执行sql语句
            conn.commit()
        except Exception as e:
            conn.rollback()
            logging.error(u"数据更新错误%s",e.message)
            raise e
        finally:
            conn.close()  # 关闭连接

    @staticmethod
    def get_conn():
        return pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='testin123',
                               db='Ontio_Test_Log', charset='utf8')



if __name__ == "__main__":
    print(DbHelper.query_one("select * from test_log"))