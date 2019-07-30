# encoding: utf-8
from core.client import HttpClient


class TestClient:

    def test_http_client(self):
        client = HttpClient(params={"method": "get"})
        assert client.params.get("method") is "get"
