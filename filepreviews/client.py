from filepreviews import exceptions
from filepreviews.session import Session


class Client(object):
    def __init__(self, api_key, api_secret, base_url):
        self.session = Session(api_key, api_secret)
        self.base_url = base_url

    def build_url(self, *args):
        return '{base_url}/{path}/'.format(
            base_url=self.base_url,
            path='/'.join(args)
        )

    def request(self, method, *args, **kwargs):
        url = self.build_url(*args)
        session_response = self.session.request(method, url, **kwargs)

        return self.process_response(session_response)

    def process_response(self, session_response):
        body = session_response.text
        status_code = session_response.status_code

        try:
            response = session_response.json()
        except Exception:
            raise exceptions.APIError(
                http_body=body,
                http_status=status_code
            )

        if not (200 <= status_code < 300):
            self.handle_api_error(body, status_code, response)

        return response

    def handle_api_error(self, body, status_code, response):
        try:
            error = response['error']
        except (KeyError, TypeError):
            raise exceptions.APIError(
                http_body=body,
                http_status=status_code,
                json_body=response
            )

        if status_code in [400, 404]:
            raise exceptions.InvalidRequestError(
                error.get('message'), error.get('param'),
                http_body=body,
                http_status=status_code,
                json_body=response
            )

        if status_code == 401:
            raise exceptions.AuthenticationError(
                error.get('message'),
                http_body=body,
                http_status=status_code,
                json_body=response
            )

        raise exceptions.APIError(
            error.get('message'),
            http_body=body,
            http_status=status_code,
            json_body=response
        )

    def get(self, *args, **kwargs):
        return self.request('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        data = kwargs.get('data')
        return self.request('POST', *args, json=data)
