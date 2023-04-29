### Design

### Architecture

The SDK is designed using a modular approach to make it flexible and extensible. It consist of the following modules:

#### api_resources
Contains an abstract Domain class with the get method in which all other classes make use of. \
The APIRequestor exposes a get method which allows us make http request from a central location  \
PathBuilder handles building the API structure based on the parameters passed

### rest
This contains various classes that extends the Domain class and corresponds to the domains on the API. \
The rest package also contains the main class of the SDK, Client.

### SDK Class
The main class of the SDK is the Client class. This class provides methods for interacting with Movie and Quote Endpoints of the API. The class is initialized with an Version, Env and API key, which is use to determine the API version, environment and used for authentication.

### Requests
The SDK provides two methods for making requests to the API domains (movie and quote). Each method corresponds to a domain in the  API. The get method takes parameters that correspond to the query string parameters of the API endpoint.
```
Client . movie  .  get()
 |         |        |
SDK      domain    method
```

### Responses
The SDK returns the response from the the-one-dev API as a Python dictionary. If an error occurs while making a request, the SDK will raise a HttpError exception.
#### Sample Response
``{status:200, json:{}}``