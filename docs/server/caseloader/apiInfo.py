# -*- coding: utf-8 -*-


class ApiInfo(object):
    def __init__(self, app_id, service_name, method, import_module_string=None, api_class=None):
        self.app_id = app_id
        self.service_name = service_name
        self.method = method
        self.import_module_string = import_module_string
        self.api_class = api_class

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        raise AttributeError(
            "attribute [%s] is not existing in %s".format(item, '.'.join([self.service_name, self.method])))


class AppIdServiceInfo(object):
    def __init__(self, app_id, service_list={}):
        self.app_id = app_id
        self.service_list = service_list
