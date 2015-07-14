import json

import pytest
import responses

from filepreviews import API_URL, FilePreviews, exceptions


file_previews = FilePreviews(
    api_key='DUMMY_API_KEY',
    api_secret='DUMMY_SECRET_KEY'
)


@responses.activate
def test_api_generate():
    def request_callback(request):
        body = {
            'id': '1',
            'status': 'pending',
            'preview': None,
            'thumbnails': None,
            'original_file': None,
            'user_data': None,
            'url': 'http://example.com/v2/previews/1/'
        }

        headers = {
            'content-type': 'application/json',
            'location': body['url']
        }

        return (201, headers, json.dumps(body))

    responses.add_callback(
        responses.POST, API_URL + '/previews/',
        callback=request_callback,
        content_type='application/json',
    )

    result = file_previews.generate('http://example.com/file.jpg')

    assert result.status == 'pending'
    assert result.url == 'http://example.com/v2/previews/1/'


@responses.activate
def test_api_retrieve():
    def request_callback(request):
        body = {
            'status': 'success',
            'thumbnails': [{
                'url': 'http://example.com/user_manual_original_1.png',
                'requested_size':
                'original',
                'resized': False,
                'original_size': {
                    'width': '612',
                    'height': '792'
                }, 'page': 1, 'size': {
                    'width': '612',
                    'height': '792'
                }
            }],
            'url': 'http://example.com/v2/previews/123/',
            'id': '123',
            'preview': {
                'url': 'http://example.com/user_manual_original_1.png',
                'requested_size': 'original',
                'resized': False,
                'original_size': {
                    'width': '612',
                    'height': '792'
                },
                'page': 1,
                'size': {
                    'width': '612',
                    'height': '792'
                }
            },
            'user_data': None,
            'original_file': {
                'mimetype': 'application/pdf',
                'name': 'user_manual',
                'extension': 'pdf',
                'encoding': 'binary',
                'total_pages': 1,
                'metadata': {},
                'type': 'application',
                'size': 416905
            }
        }

        headers = {
            'content-type': 'application/json',
            'location': body['url']
        }

        return (201, headers, json.dumps(body))

    responses.add_callback(
        responses.GET, API_URL + '/previews/123/',
        callback=request_callback,
        content_type='application/json',
    )

    result = file_previews.retrieve('123')

    assert result.status == 'success'
    assert result.url == 'http://example.com/v2/previews/123/'


@responses.activate
def test_api_error():
    def request_callback(request):
        body = 'Server Error'

        headers = {}

        return (500, headers, body)

    responses.add_callback(
        responses.POST, API_URL + '/previews/',
        callback=request_callback,
        content_type='application/json',
    )

    with pytest.raises(exceptions.APIError) as exc:
        file_previews.generate('http://example.com/file.jpg')

    assert str(exc.value) == (
        'Invalid response object from API: '
        'Server Error (HTTP response code was 500)'
    )


@responses.activate
def test_invalid_request_error():
    def request_callback(request):
        body = {
            'error': {
                'message': 'This field may not be blank.',
                'type': 'invalid_request_error',
                'param': 'url'
            }
        }

        headers = {}

        return (400, headers, json.dumps(body))

    responses.add_callback(
        responses.POST, API_URL + '/previews/',
        callback=request_callback,
        content_type='application/json',
    )

    with pytest.raises(exceptions.InvalidRequestError) as exc:
        file_previews.generate('')

    assert str(exc.value) == 'This field may not be blank.'
    assert exc.value.param == 'url'


@responses.activate
def test_authentication_error():
    def request_callback(request):
        body = {
            "error": {
                "message": "Invalid API Key provided.",
                "type": "invalid_request_error"
            }
        }

        headers = {}

        return (401, headers, json.dumps(body))

    responses.add_callback(
        responses.POST, API_URL + '/previews/',
        callback=request_callback,
        content_type='application/json',
    )

    file_previews = FilePreviews(
        api_key='WRONG_API_KEY',
        api_secret='WRONG_SECRET_KEY'
    )

    with pytest.raises(exceptions.AuthenticationError) as exc:
        file_previews.generate('http://example.com/file.jpg')

    assert str(exc.value) == 'Invalid API Key provided.'
