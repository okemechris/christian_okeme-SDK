from unittest import TestCase

from liblab_sdk_djbabs.api_resources.mixins import PathBuilder


class TestPathBuilder(TestCase):
    def test_build_pagination(self):
        t = PathBuilder(base_url="http://test.com", domain="movie", version="v2",
                        pagination={"page": 2, "limit": 100}).build()

        TestCase.assertEqual(self, first="http://test.com/v2/movie?page=2&limit=100", second=t[1])

    def test_build_sort(self):
        t = PathBuilder(base_url="http://test.com", domain="movie", version="v2",
                        sort={"name": "asc"}).build()

        TestCase.assertEqual(self, first="http://test.com/v2/movie?sort=name%3Aasc", second=t[1])

    def test_build_filter(self):
        t = PathBuilder(base_url="http://test.com", domain="movie", version="v2",
                        params={"name": {">": 10}}).build()

        TestCase.assertEqual(self, first="http://test.com/v2/movie?name>10", second=t[1])
