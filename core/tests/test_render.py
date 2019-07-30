
# encoding: utf-8
from core.utils.template_render import render_to_dict


class TestRender_variable_in_template():
    def test_render_variable_in_template(self):
        dict_or_json = {
            "value": "{{ value }}"
        }
        context = {
            "value": "test values"
        }
        params = render_to_dict(dict_or_json, context)
        assert params.get("value") == "test values"
