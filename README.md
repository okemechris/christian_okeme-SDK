# Liblab SDK

A simple SDK for accessing the the-one-api API

### Installation
```$ pip3 install -i https://test.pypi.org/simple/ liblab-djbabs==0.0.6```

### Usage
Two properties of Client have been exposed movie and quote to expose the movie and quote API
```
from liblab_sdk_djbabs.rest import Client

client = Client(version="v2", env="production", apikey="test-key")

res = client.movie.get()

print(res)

res = client.quote.get()

print(res)
```
### Parameters
domain_id (string):\
Used to retrieve one record\
``client.movie.get(domain_id=11277636664)``

pagination (Object):\
Used to handle pagination\
```client.movie.get(pagination={"page": 1, "limit": 10, "offset":1})```

sort (Object): \
The sort parameter is used to sort response from the API
```client.movie.get(sort={"name":"asc"}})```

### Filtering and other Parameters
the params parameter is used to filter or pass other query parameters \
Allowed operators \
[ =, !=, e, >, >=, <=, ! ]
#### usage
params={ field : { operator : value } }

```client.movie.get(params={"name":{"=":"Test"}})```

### Test
To run the tests included do the following
```
$ cd src/liblab_sdk_djbabs
$ python3 -m unittest discover -s ../tests
```

