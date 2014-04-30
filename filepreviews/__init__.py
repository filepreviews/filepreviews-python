import os
import json
import hashlib
import logging

try:
    # Python 3
    from urllib.parse import urlencode
    from urllib.error import HTTPError
    from urllib.request import urlopen
except ImportError:
    # Python 2
    from urllib import urlencode, urlopen
    from urllib2 import HTTPError


__version__ = '1.0.2'
VERSION = __version__

API_URL = 'https://blimp-previews.herokuapp.com'
RESULTS_URL = 'https://s3.amazonaws.com/demo.filepreviews.io'

logger = logging.getLogger('filepreviews')


class FilePreviews(object):
    def __init__(self, *args, **kwargs):
        self.debug = kwargs.get('debug', False)
        self.api_url = kwargs.get('api_url', API_URL)
        self.results_url = kwargs.get('results_url', RESULTS_URL)

        if self.debug:
            logging.basicConfig(level=logging.DEBUG)

        logger.debug('Initializing FilePreviews')

    def generate(self, url, **kwargs):
        logger.debug('Generating preview for {}'.format(url))

        request_url = self._generate_request_url(url, **kwargs)

        try:
            response = urlopen(request_url)
            preview_url = response.geturl()
        except HTTPError as response:
            preview_url = response.geturl()

        return {
            'metadata': self._poll_for_metadata(url, **kwargs),
            'preview_url': preview_url
        }

    def _generate_request_url(self, url, **kwargs):
        metadata = set(kwargs.get('metadata', []))
        size = kwargs.get('size')
        params = {
            'url': url
        }

        if metadata:
            params['metadata'] = ','.join(metadata)

        if size:
            width = size.get('width')
            height = size.get('height')
            geometry = ''

            if width:
                geometry = width

            if height:
                geometry = '{}x{}'.format(geometry, height)

            params['size'] = geometry

        return '{}/?{}'.format(self.api_url, urlencode(params))

    def _generate_url_hash(self, url, **kwargs):
        request_url = self._generate_request_url(url, **kwargs)
        return hashlib.sha256(request_url.encode('utf-8')).hexdigest()

    def _generate_metadata_url(self, url, **kwargs):
        url_hash = self._generate_url_hash(url, **kwargs)
        return '{}/{}/metadata.json'.format(self.results_url, url_hash)

    def _poll_for_metadata(self, url, **kwargs):
        metadata_url = self._generate_metadata_url(url, **kwargs)

        logger.debug('Polling {}'.format(metadata_url))

        try:
            response = urlopen(metadata_url)
            data = response.read()
            return json.loads(data.decode('utf-8'))
        except HTTPError:
            return self._poll_for_metadata(url, **kwargs)
