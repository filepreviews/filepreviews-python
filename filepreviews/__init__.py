import json
import logging

try:
    # Python 3
    from urllib.error import HTTPError
    from urllib.request import urlopen, Request
except ImportError:
    # Python 2
    from urllib2 import Request, urlopen, HTTPError


__version__ = '1.1.0'
VERSION = __version__

API_URL = 'https://api.filepreviews.io/v1/'

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

        try:
            request = self._generate_request(url, **kwargs)
            response = urlopen(request)
            data = self._get_json_response(response)
        except HTTPError as response:
            return self._get_json_response(response)

        return {
            'metadata': self._poll_metadata(data['metadata_url'], **kwargs),
            'preview_url': data['preview_url']
        }

    def _generate_request(self, url, **kwargs):
        metadata = set(kwargs.pop('metadata', []))
        size = kwargs.pop('size', None)
        params = {
            'url': url,
            'metadata': list(metadata)
        }

        if size:
            width = size.get('width')
            height = size.get('height')
            geometry = ''

            if width:
                geometry = width

            if height:
                geometry = '{}x{}'.format(geometry, height)

            params['sizes'] = [geometry]

        params.update(kwargs)

        headers = {
            'Content-Type': 'application/json',
        }

        data = json.dumps(params).encode('utf-8')

        request = Request(self.api_url, data, headers)

        if self.api_key:
            request.add_header('X-API-Key', self.api_key)

        return request

    def _poll_metadata(self, metadata_url, **kwargs):
        logger.debug('Polling {}'.format(metadata_url))

        try:
            response = urlopen(metadata_url)
            return self._get_json_response(response)
        except HTTPError:
            return self._poll_metadata(metadata_url, **kwargs)

    def _get_json_response(self, response):
        return json.loads(response.read().decode('utf-8'))
