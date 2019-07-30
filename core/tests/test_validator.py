# encoding: utf-8
from core import validator


class TestValidator():

    def test_demos(self):
        result = validator.validate("value","is_equal_to test")
        assert result[0],"fail"
        print(str(result[1]))
