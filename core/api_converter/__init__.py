# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :        patrick
   date：          2019/7/10
-------------------------------------------------
   Change Activity:
                   2019/7/10:
-------------------------------------------------
"""
__author__ = 'patrick'

runner_api_template = """class $name(HttpClient):
                            method = "$method"
                            req_url = "$req_url"
                            req_body= $req_body
                            headers = ${headers} 
                    """
