import logging

from filepreviews import API_URL
from filepreviews.client import Client
from filepreviews.models import PreviewResult


logging.getLogger('requests').setLevel(logging.WARNING)


class FilePreviews(object):
    def __init__(self, api_key=None, api_secret=None, **kwargs):
        api_url = kwargs.get('api_url', API_URL)
        debug = kwargs.get('debug')

        self.client = Client(api_key, api_secret, api_url)
        self.logger = logging.getLogger('filepreviews')

        if debug:
            logging.basicConfig(level=logging.INFO)

        self.logger.info('Initializing FilePreviews')

    def generate(self, url, **kwargs):
        self.logger.info('Generating preview for {0}'.format(url))

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

        response = self.client.post('previews', data=params)

        return PreviewResult(response)

    def retrieve(self, preview_id):
        self.logger.info('Retrieving preview {0}'.format(preview_id))

        response = self.client.get('previews', preview_id)

        return PreviewResult(response)
