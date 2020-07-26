# -*- coding: utf-8 -*-
from docs.server import BaseCollection


class APIDesc(BaseCollection):
    collection_name = 'api_descs'

    def __init__(self, api_desc):
        super(APIDesc, self).__init__()
        self.collection_doc = api_desc
        self.api_name = api_desc['apiName']
        self.path_parameters = api_desc['pathParameters']
        self.response_body = api_desc['responseBody']
        self.api_description = api_desc['apiDescription']
        self.api_request_body = api_desc['requestBody']
        self.resource_url = api_desc['resourceUrl']
        self.headers = api_desc['headers']
        self.request_method = api_desc['requestMethod']
        self.query_parameters = api_desc['queryParameters']

    def update_or_insert(self):
        result = self.find(params={"apiName": self.collection_doc['apiName']})
        if result:
            self.update()
        else:
            self.insert_one(self.collection_doc)

    def update(self):
        self.update_one(search_criteria={"apiName": self.collection_doc['apiName']})
