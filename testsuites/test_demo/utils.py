# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     utils
   Description :
   Author :        patrick
   date：          2019/8/14
-------------------------------------------------
   Change Activity:
                   2019/8/14:
-------------------------------------------------
"""
import time

__author__ = 'patrick'


def business_no():
    return str(time.time() / 100)


def batch_id(prefix):
    return prefix + str(business_no())

#
# if __name__ == '__main__':
#     print(business_no())
#     print(batch_id("test"))
