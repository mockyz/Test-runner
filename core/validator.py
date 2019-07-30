# encoding: utf-8
from core.utils.assertpy import assert_that


def validate(check_value, expected_exp):
    """
    use assertpy to assert
    todo: need handle different type,like types
    """

    validator = assert_that(check_value)
    func_param_map = expected_exp.split(" ")
    func = getattr(validator, func_param_map[0])
    params = expected_exp[len(func_param_map[0]) + 1:].lstrip()
    try:
        if params == "":
            return "success", func()
        return "success", func(params)
    except AssertionError as err:
        return "failed", err
