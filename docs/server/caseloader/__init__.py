# -*- coding: utf-8 -*-

"""
This package is used for read the api classes and corresponded api test cases
"""
import inspect
import os

from base.api_base_client import BaseAPI
from server.caseloader.apiInfo import ApiInfo, AppIdServiceInfo

# base module path of apis
api_module_path = './../../modules/'

# base module name of apis
api_base_module_name = 'modules'

"""
key: app_id
value: folders which have the apis in this app_id
"""

appId_module_mapping = {
    "napos.shop.api.melody": ['shop', 'goods'],
    "napos.marketing.api.melody": ['marketing'],
    "napos.order.api.melody": ['orders'],
    "napos.delivery.api.melody": ['delivery']
}

"""
default module and test folder mapping is that module folder name should be same as test folder name
this mapping override the default mapping:
key: service module
value: the real test module to the corresponded service module
"""
module_test_override_mapping = {
    "modules.goods.food": "test.goods.goods_detail",
    "modules.goods.food_chain": "test.goods.goods_chain_detail"
}


def load_all_apis():
    """
    load all api info entry point
    :return: {}, key:app_id,value: all the napos apis in this app_id
    """
    all_apis = dict()
    for app_id in appId_module_mapping:
        all_apis[app_id] = dict()
        for folder in appId_module_mapping[app_id]:
            for root, directory, service_modules in os.walk(os.path.join(api_module_path, folder)):
                if len(service_modules) > 1 and not root.endswith('__pycache__'):
                    all_apis[app_id].update(get_naposapis_in_app(app_id, service_modules, folder))
    return all_apis


def get_naposapis_in_app(app_id, service_modules, parent_module):
    """
    get service classes files in one module
    :param service_modules:
    :param parent_module:
    :return: {},key: app_id, value: all the napos apis in the given app_id
    """
    api_services = dict()
    for service_file in service_modules:
        if not service_file.startswith('__') and not service_file.endswith('.pyc'):
            service_py_name = service_file[:-3]
            import_module_path = '.'.join([api_base_module_name, parent_module, service_py_name])
            service_apis = get_naposapis_in_module(app_id, import_module_path)
            api_services.update(service_apis)
    return api_services


def get_naposapis_in_module(app_id, import_module_path, module_imported=None):
    """
    get napos api classes in one module
    :param app_id:
    :param import_module_path:
    :return: dict, key: app_id, value: list of napos api classes in this module
    """
    if module_imported is None:
        module_imported = __import__(import_module_path)
    api_info_result = {}
    for member, data in inspect.getmembers(module_imported):
        # ignore env module to avoid Endless recursion
        if not member.startswith("__") and not member == 'env':
            if inspect.ismodule(data):
                api_info_result.update(
                    get_naposapis_in_module(app_id, module_imported=data,
                                            import_module_path=import_module_path))
                continue

            if inspect.isclass(data):
                try:
                    if issubclass(data, BaseAPI) and data.__name__ != BaseAPI.__name__:
                        api_info = ApiInfo(app_id, service_name=data.service, method=data.__name__,
                                           import_module_string=import_module_path, api_class=data)
                        if api_info_result.get(data.service) is None:
                            api_info_result[data.service] = []
                        api_info_result[data.service].append(api_info)
                except Exception as e:
                    print("error happened for [%s],error=%s".format(data, e))

    return api_info_result


all_apis = load_all_apis()


def get_testcases_files(api_info):
    """
    get test cases files by the given api_info,
    the default mapping rule for api and api test is:
    api module path is like this: modules.<module>.<service_name>.<method>
    api test module path is like this: test.<module>.<service_name>.test_<method>
    but for some tests, it is not true, so combine the api test module which path is test.<module>.test_<service_name>
    :param api_info:
    :return: [],list of test case files path
    """
    result = []
    test_module = module_test_override_mapping.get(api_info.import_module_string, api_info.import_module_string)
    test_module = test_module.replace('modules', 'test').replace('.', '/')


def get_api_info(app_id, service_name, method):
    """
    get api info by appid,service name, method from the all_apis
    :param app_id:
    :param service_name:
    :param method:
    :return: ApiInfo instance
    """
    for api_info in all_apis[app_id]:
        if api_info.service_name.lowcase() == service_name.lowcase() and api_info.method.lowcase() == method.lowcase():
            return api_info
    raise Exception(
        "can't find api test for :app_id:[%s],service:[%s],method:[%s]".format(app_id, service_name, method))
