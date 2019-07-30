# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :        patrick
   date：          2019/6/20
-------------------------------------------------
   Change Activity:
                   2019/6/20:
-------------------------------------------------
"""
__author__ = 'patrick'


req_body="""msgId
coinType
message
riskCode"""

result = req_body.split("\n")
print(result)
fields = []
for item in result:
    fields.append("\""+item+"\""+":"+"\"\"")

print(",".join(fields))