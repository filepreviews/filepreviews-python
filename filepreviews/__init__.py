import json
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


__version__ = '1.0.4'
VERSION = __version__

API_URL = 'https://blimp-previews.herokuapp.com'

logger = logging.getLogger('filepreviews')


class FilePreviews(object):
    def __init__(self, *args, **kwargs):
        self.debug = kwargs.get('debug', False)
        self.api_url = kwargs.get('api_url', API_URL)

        if self.debug:
            logging.basicConfig(level=logging.DEBUG)

        logger.debug('Initializing FilePreviews')

    def generate(self, url, **kwargs):
        logger.debug('Generating preview for {}'.format(url))

        request_url = self._generate_request_url(url, **kwargs)

        try:
            response = urlopen(request_url)
            data = self._get_json_response(response)
        except HTTPError as response:
            data = self._get_json_response(response)

        return {
            'metadata': self._poll_metadata(data['metadata_url'], **kwargs),
            'preview_url': data['preview_url']
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

    def _poll_metadata(self, metadata_url, **kwargs):
        logger.debug('Polling {}'.format(metadata_url))

        try:
            response = urlopen(metadata_url)
            return self._get_json_response(response)
        except HTTPError:
            return self._poll_metadata(metadata_url, **kwargs)

    def _get_json_response(self, response):
        return json.loads(response.read().decode('utf-8'))
