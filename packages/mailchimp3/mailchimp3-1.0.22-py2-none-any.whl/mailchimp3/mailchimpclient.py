"""
Mailchimp v3 Api SDK

"""

from __future__ import unicode_literals

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import InvalidURL, HTTPError
# Handle library reorganisation Python 2 > Python 3.
try:
    from urllib.parse import urljoin
    from urllib.parse import urlencode
except ImportError:
    from urlparse import urljoin
    from urllib import urlencode


class MailChimpClient(object):
    """
    MailChimp class to communicate with the v3 API
    """

    def __init__(self, mc_user, mc_secret):
        """
        Initialize the class with you user_id and secret_key
        """
        super(MailChimpClient, self).__init__()
        self.auth = HTTPBasicAuth(mc_user, mc_secret)
        datacenter = mc_secret.split('-').pop()
        self.base_url = 'https://%s.api.mailchimp.com/3.0/' % datacenter

    def _post(self, url, data=None):
        """
        Handle authenticated POST requests
        """
        url = urljoin(self.base_url, url)
        r = requests.post(url, auth=self.auth, json=data)
        if r.status_code == requests.codes.ok:
            return r.json()
        if r.status_code == requests.codes.no_content:
            return "{'status': 204}"
        else:
            raise HTTPError(request=r)

    def _get(self, url, **queryparams):
        """
        Handle authenticated GET requests
        """
        url = urljoin(self.base_url, url)

        if len(queryparams):
            url += '?' + urlencode(queryparams)

        try:
            r = requests.get(url, auth=self.auth)
        except InvalidURL as e:
            raise e
        return r.json()

    def _delete(self, url):
        """
        Handle authenticated DELETE requests
        """
        url = urljoin(self.base_url, url)
        r = requests.delete(url, auth=self.auth)
        r.raise_for_status()
        if r.text:
            return r.json()
        else:
            return

    def _patch(self, url, data=None):
        """
        Handle authenticated PATH requests
        """
        url = urljoin(self.base_url, url)
        r = requests.patch(url, auth=self.auth, json=data)
        return r.json()

    def _put(self, url, data=None):
        """
        Handle authenticated PUT requests
        """
        url = urljoin(self.base_url, url)
        r = requests.put(url, auth=self.auth, json=data)
        return r.json()
