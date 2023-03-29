from unittest import TestCase
from unittest.mock import patch

from django.core.cache import cache

from memberpress_client.client import MemberpressAPIClient

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data
    
    def raise_for_status(self):
        pass


class TestClient(TestCase):

    def setUp(self):
        cache.clear()

    @patch("memberpress_client.client.requests.get", return_value=MockResponse({"foo": "bar"}, 200))
    def test_response_caching(self, mock_get):
        client = MemberpressAPIClient()
        assert mock_get.call_count == 0
        # first call should make a request
        client.get("test")
        assert mock_get.call_count == 1
        # second call should retrieve from cache
        client.get("test")
        assert mock_get.call_count == 1
        # first call with params should make a request
        client.get("test", params={"param_1": "value_1"})
        assert mock_get.call_count == 2
        # second call with params should retrieve from cache
        client.get("test", params={"param_1": "value_1"})
        assert mock_get.call_count == 2