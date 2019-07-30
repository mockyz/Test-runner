# encoding: utf-8
import json

import jsonpickle

from . import data_extractor


class KVUtil:
    @staticmethod
    def get_value(kv, expression):
        return data_extractor.get_value_by_exp(kv, expression)

    @staticmethod
    def set_value(kv, expr, value):
        """
        assume expression is ***.***
        :param kv:
        :param expr:
        :param value:
        :return:
        """
        data_paths = expr.split(".")
        depth = len(data_paths)
        data = kv
        for index in range(depth - 1):
            if data.get(data_paths[index], "") != "":
                data = data.get(data_paths[index])
            else:  ## ignore not existing value
                return
        data[data_paths[depth - 1]] = value

    """Search for a key inside a dictionary, visiting it in a recursive way
    and return the value of this key.
    d: dictionary to search into
    kname: key name to search for
    """

    def dict_search_value(self, d, kname):
        if type(d) == dict:
            for k, v in d.items():
                if type(v) == dict:
                    value = self.dict_search_value(v, kname)
                    if value:
                        return value
                if type(v) == list:
                    if len(v) > 0:
                        for element in v:
                            if type(element) == dict:
                                value = self.dict_search_value(element, kname)
                                if value:
                                    return value
                if k == kname:
                    return v

    """Given a list of fields/keys and two dictionaries, it searches for each key in both
    dictionaries and assert as equal the found value.
    fields: a list of fields/keys to verify
    dict_1: first dictionary
    dict_2: second dictionary
    """

    def compare_assert_dicts(self, fields, dict_1, dict_2):
        for f in fields:
            value_dict1 = self.dict_search_value(dict_1, f)
            value_dict2 = self.dict_search_value(dict_2, f)

            if type(value_dict1) is list:
                value_dict1 = list(value_dict1).sort()
            if type(value_dict2) is list:
                value_dict2 = list(value_dict2).sort()

            # self.assertEqual(value_dict1, value_dict2,
            #                  "Returned value: %s, expected value: %s" % (str(value_dict1), str(value_dict2)))


class EasyKVObject:

    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)

    def to_json_with_module(self):
        return jsonpickle.encode(self)

    def to_dict(self):
        return json.loads(self.to_json(), encoding="utf-8")


kv_util = KVUtil()
