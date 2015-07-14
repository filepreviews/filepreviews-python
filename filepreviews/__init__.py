# -*- coding: utf-8 -*-
# flake8: noqa
"""
A Python library for FilePreview's API.
"""

__title__ = 'filepreviews'
__version__ = '2.0.0'
__author__ = 'José Padilla'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Blimp LLC'


VERSION = __version__
API_URL = 'http://192.168.59.103:8000/v2'

from .api import FilePreviews
from .exceptions import (
    FilePreviewsError, APIError, InvalidRequestError, AuthenticationError
)
