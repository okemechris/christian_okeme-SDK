from liblab_sdk_djbabs.api_resources.mixins import PathBuilder
from liblab_sdk_djbabs.api_resources.api_requester import APIRequestor


class Client(object):
    """
    A client for accessing the the-one-api API.
    """

    def __init__(
            self,
            version=None,
            env=None,
            apikey=None
    ):
        """
        Initializes the liblab_sdk Client
        :param str version: liblab_sdk version
        :param str env: The environment in which API calls will be made
        :param str apikey: The apikey for your the-one-api account
        :returns: liblab_sdk Client
        :rtype: liblab_sdk.rest.Client
        """
        self.liblab_sdk_version = version
        self.env = env
        self.apikey = apikey

        base_url = {
            "production": 'https://the-one-api.dev',
            "test": 'https://the-one-api.dev',
        }
        try:
            self.base_url = base_url[self.env.strip().lower()]
        except AttributeError:
            raise Exception("Use 'production' or 'test' as env")

        # Domains
        self._movie = None
        self._movie_quote = None
        self._quote = None

    def request(self, method, base_url, domain, version, pagination=None, sort=None, domain_id=None, domain_action=None,
                params=None, headers=None, data=None):

        params = params or {}
        method = method.upper()
        pagination = pagination or {}
        headers = headers or {}
        sort = sort or {}

        path, url = PathBuilder(
            base_url=base_url,
            domain=domain,
            version=version,
            pagination=pagination,
            sort=sort,
            domain_id=domain_id,
            domain_action=domain_action,
            params=params).build()

        api = APIRequestor(url=url, headers={'Authorization': f"Bearer {self.apikey}"})

        if method == "GET":
            response = api.get()
        else:
            raise Exception(f'Method {method} not supported')

        json_response = {}

        if method != "DELETE":
            if response.ok:
                json_response = response.json()
            else:
                response.raise_for_status()

        return {
            "status": response.status_code,
            "json": json_response
        }

    @property
    def movie(self):
        """
        Access the the-one-api Movie API
        """
        if self._movie is None:
            from liblab_sdk_djbabs.rest.movie import Movie
            self._movie = Movie(self, self.base_url, 'movie', self.liblab_sdk_version)
        return self._movie

    @property
    def quote(self):
        """
        Access the the-one-api Quote API
        """
        if self._quote is None:
            from liblab_sdk_djbabs.rest.quote import Quote
            self._quote = Quote(self, self.base_url, 'quote', self.liblab_sdk_version)
        return self._quote
