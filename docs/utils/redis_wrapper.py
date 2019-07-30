# -*- coding: utf-8 -*-
import json

import redis


class RedisWrapper(object):
    def __init__(self, host, port=6379, db=0):
        self.redis_client = redis.Redis(host=host, port=port, db=0)

    @staticmethod
    def get_redis(host, port=6379, db=0):
        return RedisWrapper(host, port, db)

    def invoke(self, params={}):
        """
        params: {"command":"redis command"}
        :param params:
        :return:
        """
        command = params.get('command')
        key = params.get('key')
        value = params.get('value')
        if value and key:
            result = self.redis_client.execute_command(command, key, value)
        elif key and not value:
            result = self.redis_client.execute_command(command, key)
        else:
            result = self.redis_client.execute_command(command)

        if isinstance(result, bytes):
            try:
                return json.dumps(eval(result.decode('utf-8')))
            except:
                return {"result": result.decode('utf-8')}
        else:
            return {"result": "OK"}
