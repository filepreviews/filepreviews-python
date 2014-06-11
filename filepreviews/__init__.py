import json
import logging

try:
    # Python 3
    from urllib.parse import urlencode
    from urllib.error import HTTPError
    from urllib.request import urlopen, Request
except ImportError:
    # Python 2
    from urllib import urlencode, urlopen, Request
    from urllib2 import HTTPError


__version__ = '1.0.5'
VERSION = __version__

API_URL = 'https://api.filepreviews.io/v1'

logger = logging.getLogger('filepreviews')


class FilePreviews(object):
    def __init__(self, *args, **kwargs):
        self.debug = kwargs.get('debug', False)
        self.api_url = kwargs.get('api_url', API_URL)
        self.api_key = kwargs.get('api_key')

        if self.debug:
            logging.basicConfig(level=logging.DEBUG)

        logger.debug('Initializing FilePreviews')

    def generate(self, url, **kwargs):
        logger.debug('Generating preview for {}'.format(url))

        request_url = self._generate_request_url(url, **kwargs)

        try:
            request = Request(request_url)

            if self.api_key:
                request.add_header('X-API-Key', self.api_key)

            response = urlopen(request)
            data = self._get_json_response(response)
        except HTTPError as response:
            return self._get_json_response(response)

        return {
            'metadata': self._poll_metadata(data['metadata_url'], **kwargs),
            'preview_url': data['preview_url']
        }

    def _generate_request_url(self, url, **kwargs):
        metadata = set(kwargs.pop('metadata', []))
        size = kwargs.pop('size', None)
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

        params.update(kwargs)

        return '{}/?{}'.format(self.api_url, urlencode(params))

    def _poll_metadata(self, metadata_url, **kwargs):
        logger.debug('Polling {}'.format(metadata_url))

        try:
            response = urlopen(metadata_url)
            return self._get_json_response(response)
        except HTTPError:
            return self._poll_metadata(metadata_url, **kwargs)

    def _get_json_response(self, response):
        return json.loads(response.read().decode('utf-8'))
