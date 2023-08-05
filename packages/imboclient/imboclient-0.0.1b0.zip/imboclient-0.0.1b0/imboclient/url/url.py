from imboclient.url import accesstoken
import urllib.parse
import json

class Url(object):
    def __init__(self, base_url, public_key, private_key):
        self._base_url = base_url
        self._public_key = public_key
        self._private_key = private_key
        self._query_params = None

    def __str__(self):
        return self.url()

    def url(self):
        url = self.resource_url()
        query_string = self.query_string()

        if self._query_params and len(self._query_params) > 0:
            url = url + '?' + query_string

        if self._public_key == None or self._private_key == None:
            return url

        self.access_token = accesstoken.AccessToken()
        generated_token = self.access_token.generate_token(url, self._private_key)

        if self._query_params == None:
            return url + '?accessToken=' + generated_token

        return url + '&accessToken=' + generated_token

    def add_query_param(self, key, value):
        if (self._query_params == None):
            self._query_params = []

        self._query_params.append((key, value))
        return self

    def add_query(self, query):
        if query:
            self.add_query_param('page', query.page())
            self.add_query_param('limit', query.limit())
            self.add_query_param('from', query.q_from())
            self.add_query_param('to', query.q_to())
        if query.metadata:
            self.add_query_param('query', json.dumps(query.query()))

        return self

    def query_string(self):
        if not self._query_params:
            return ''
        return urllib.parse.urlencode(self._query_params)

    def resource_url(self):
        raise NotImplementedError("Missing implementation. You may want to use a Url implementation instead.")

    def reset(self):
        self._query_params = []
        return self

