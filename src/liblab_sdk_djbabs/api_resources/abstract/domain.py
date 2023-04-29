class Domain(object):
    """
    Abstract class used in each domain/endpoint
    Makes an HTTP request to this domain.
        :param dict params: Query parameters.
        :param object data: The request body.
        :param dict headers: The HTTP headers.
        :param tuple auth: Basic auth tuple of (api_key, secret)
    """

    def __init__(self, liblab_sdk_djbabs):
        self.liblab_sdk = liblab_sdk_djbabs

    def get(self, params=None, data=None, headers=None,sort=None, pagination=None, domain_id=None, domain_action=None):
        return self.liblab_sdk.request(
            'get',
            self.base_url,
            self.domain,
            self.version,
            params=params,
            data=data,
            headers=headers,
            pagination=pagination,
            sort=sort,
            domain_id=domain_id,
            domain_action=domain_action
        )
