# encoding: utf-8
import json

from jinja2 import Template


def render_template(temp_str, context):
    template = Template(temp_str)
    return template.render(context)


def render_to_dict(dict_or_json, context):
    template = Template(json.dumps(dict_or_json))
    filled_str = template.render(context)
    return json.loads(filled_str, encoding='utf-8')
