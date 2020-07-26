# encoding: utf-8
from .utils.kv_utils import kv_util

ENV_TEST = "TEST"
ENV_PROD = "PROD"
ENV_STAGE = "STAGE"

environments = {
    "test": {
        "domain": "http://httpbin.org",
        "candybox": "https://candyapit.ont.io",
        "WALLET_SERVER": "https://42.159.155.44:8443",
        "ONTRADE_SERVER": "https://42.159.155.44:8443",
        "db": {"ontpass": "mysql://readonly:ZEwyRiwCZDWBdA==@128.1.132.227/ontpass"},
        "VTribe":"http://47.100.0.26:8081"

    },
    "prod": {
        "domain": "http://httpbin.org",
        "candybox": "https://candyapi.ont.io",
        "ontoservice": "https://app.ont.io"
    }, "dev": {
        "domain": "http://httpbin.org",
        "ontoservice": "https://app.ont.io/S1"
    }
}


class TargetEnvironment:

    def __init__(self, env="test"):
        self.env = env
        self.configs = environments.get(env.lower())

    def get_config_by_key(self, key_or_expr):
        """
        get configured environment
        :param key_or_expr: a key or a expresion
        :return:
        """
        return kv_util.get_value(self.configs, key_or_expr)


TEST_ENV = TargetEnvironment("test")
PROD_ENV = TargetEnvironment("prod")
DEV_ENV = TargetEnvironment("dev")
