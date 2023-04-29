from unittest import TestCase
import requests


class TestClient(TestCase):
    def test_movie_bad_credential(self):
        from liblab_sdk_djbabs.rest import Client
        c = Client(version="v2", env="test", apikey="fake-key")
        with self.assertRaises(requests.exceptions.HTTPError):
            c.movie.get()



