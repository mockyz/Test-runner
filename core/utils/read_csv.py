import os
import time

import pandas as pd
import pymysql

from core.utils.DbHelper import DbHelper


inset_sql = r"INSERT test_log (case_name,execute_status,log_path,test_suite) values('%s'," \
             "'%s','%s','%s')"
# noinspection SqlDialectInspection
create_table = r"CREATE TABLE `%s` ( `case_name`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ," \
               r"`execute_status`  varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,`log_path`  varchar(150) " \
               r"CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL ,`test_suite`  varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci " \
               r"NULL DEFAULT NULL )ENGINE=InnoDB DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci ROW_FORMAT=DYNAMIC;"


def GetFile2(dir):
    if os.path.isfile(dir) and "collection_log" in dir:
        datas = pd.read_csv(dir)
        path = dir.split('\\')
        for data in datas.values:
            values = (data[0], data[1], pymysql.escape_string(dir[0:-18]+(data[2])), path[-2])
            exe_sql = (inset_sql % values)
            print(exe_sql)
            DbHelper.execute_sql(exe_sql)

    if os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            GetFile2(newDir)


if __name__ == '__main__':
    #
    # tName = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
    # DbHelper.execute_sql(create_table % tName)
    GetFile2('C:\\Users\\mock\\Desktop\\工作台\\Ontology\\1.7.2\\9-20-172\\')

