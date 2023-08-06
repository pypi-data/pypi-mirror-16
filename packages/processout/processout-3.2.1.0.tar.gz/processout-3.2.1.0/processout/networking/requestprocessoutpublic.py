import requests
try:
    import urllib.parse
except ImportError:
    import urllib

from ..processout import ProcessOut

class RequestProcessoutPublic:
    def __init__(self, instance):
        """Create a new Request instance

        Keyword argument:
        instance -- ProcessOut instance
        """
        self._instance = instance

    def _authenticate(self):
        """Return the correct needed authentication"""
        username = self._instance.projectId
        password = ''
        return (username, password)

    def _getHeaders(self, options):
        """Return the headers sent with the request"""
        headers = {}
        headers["API-Version"] = "1.1.0.0"

        if options is None:
            return headers

        if "idempotency_key" in options:
            headers["Idempotency-Key"] = options["idempotency_key"]

        return headers

    def get(self, path, data, options):
        """Perform a GET request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        options -- Options sent with the request
        """
        return requests.get(self._instance.host + path + '?' +
                urllib.urlencode(data),
            auth   = self._authenticate(),
            verify = True,
            headers = self._getHeaders(options))

    def post(self, path, data, options):
        """Perform a POST request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        options -- Options sent with the request
        """
        return requests.post(self._instance.host + path,
            auth   = self._authenticate(),
            json   = data,
            verify = True,
            headers = self._getHeaders(options))

    def put(self, path, data, options):
        """Perform a PUT request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        options -- Options sent with the request
        """
        return requests.put(self._instance.host + path,
            auth   = self._authenticate(),
            json   = data,
            verify = True,
            headers = self._getHeaders(options))

    def delete(self, path, data, options):
        """Perform a DELETE request

        Keyword argument:
        path -- Path of the request
        data -- Data to be passed along with the request
        options -- Options sent with the request
        """
        return requests.delete(self._instance.host + path + '?' +
                urllib.urlencode(data),
            auth   = self._authenticate(),
            verify = True,
            headers = self._getHeaders(options))
