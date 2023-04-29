from liblab_sdk_djbabs.api_resources.abstract.domain import Domain


class Movie(Domain):

    def __init__(self, liblab_sdk_djbabs, base_url, domain, version, **kwargs):
        """
        Initialize the Movie Domain
        """
        super(Movie, self).__init__(liblab_sdk_djbabs)
        self.base_url = base_url
        self.domain = domain
        self.version = version

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<liblab_sdk.Movie>'
