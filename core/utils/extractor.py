# encoding: utf-8
import jmespath
from dictor import dictor


def search_by_jmespath(dict_or_json, expr):
    jmespath_expr = jmespath.compile(expr)
    return jmespath_expr.search(dict_or_json)


extractor_engine = {
    "dictor": dictor,
    "jmespath": search_by_jmespath
}


class DataExtractor:

    def __init__(self):
        pass

    @staticmethod
    def get_value_by_exp(dict_or_json, expr, type="dictor"):
        """
        use dictor or jmespath to get value
        :param dict_or_json:
        :param expr: dictor expression or jmespath expression
        :param type: different parse engine for dict or json
        :return:
        """

        try:
            return extractor_engine.get(type, "dictor")(dict_or_json, expr)
        except Exception as e:  ## fail over
            for key, extractor in extractor_engine.items():
                if key != "dictor":
                    return extractor(dict_or_json, expr)


data_extractor = DataExtractor()
