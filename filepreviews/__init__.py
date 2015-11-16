# -*- coding: utf-8 -*-
# flake8: noqa
"""
A Python library for FilePreview's API.
"""

__title__ = 'filepreviews'
__version__ = '2.0.2'
__author__ = 'José Padilla'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Blimp LLC'


VERSION = __version__
API_URL = 'https://api.filepreviews.io/v2'

from .api import FilePreviews
from .exceptions import (
    FilePreviewsError, APIError, InvalidRequestError, AuthenticationError
)
