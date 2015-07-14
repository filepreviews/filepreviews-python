import requests
from requests.auth import HTTPBasicAuth


class Session(requests.Session):
    def __init__(self, api_key, api_secret):
        super(Session, self).__init__()
        self.auth = HTTPBasicAuth(api_key, api_secret)
