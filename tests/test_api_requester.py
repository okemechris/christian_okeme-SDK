from unittest import TestCase

from liblab_sdk_djbabs.api_resources.api_requester import APIRequestor


class TestAPIRequestor(TestCase):
    def test_get(self):
        api = APIRequestor(method="GET", url="https://www.google.com")
        res = api.get()
        TestCase.assertEqual(self, first=res.status_code, second=200)
