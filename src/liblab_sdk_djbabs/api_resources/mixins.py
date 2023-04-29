import json
import urllib
from urllib.parse import urlencode


def create_params(**kwargs):
    """
    Used to create url parameters for API call
    """
    url = kwargs.get("url")
    params = kwargs.get("params")
    operator = kwargs.get("operator") or '='

    if params:
        query_string = custom_urlencode(eval(params), operator)

    return f'{url}?{query_string}'

def custom_urlencode(params, operator):
    encoded_params = []
    for key, value in params.items():
        key = urllib.parse.quote(key, safe='')
        value = urllib.parse.quote(str(value), safe='')
        encoded_params.append(key + operator + value)
    return '&'.join(encoded_params)


class PathBuilder:

    def __init__(self, **kwargs):
        self.base_url = kwargs.get('base_url')
        self.domain = kwargs.get('domain')
        self.version = kwargs.get('version')
        self.domain_id = kwargs.get("domain_id")
        self.domain_action = kwargs.get("domain_action")
        self.params = kwargs.get('params') or {}
        self.pagination = kwargs.get('pagination') or {}
        self.sort = kwargs.get('sort') or {}


    def build(self):
        paths = {
            "domains": {
                "movie": {
                    "path": f'{self.version}/movie',
                },
                "quote": {
                    "path": f'{self.version}/quote',
                }
            }

        }

        domain_info = paths['domains'][self.domain]
        sections = [domain_info['path']]
        if self.domain_id:
            sections.append(self.domain_id)
            if self.domain_action:
                sections.append(self.domain_action)

        path = f'/{"/".join(sections)}'
        url = f'{self.base_url}{path}'

        # manage params and filtering
        params = {}
        operators = ["=", "!=", "e", ">", ">=", "<=", "!"]
        pagination_operators = ["page", "limit", "offset"]
        sorting_operators = ["desc", "asc"]

        for p in self.pagination.keys():
            if p in pagination_operators:
                params[p] = f'{self.pagination[p]}'

        for s in self.sort.keys():
            if self.sort[s] in sorting_operators:
                params['sort'] = f'{s}:{self.sort[s]}'

        operator = None
        for param in self.params.keys():
            for k in self.params[param].keys():
                if k in operators:
                    params[f'{param}'] = f'{self.params[param][k]}'
                    operator = k

        if params:
            url = create_params(params=json.dumps(params), url=url, operator=operator)

        return [path, url]
