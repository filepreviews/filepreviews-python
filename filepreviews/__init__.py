# -*- coding: utf-8 -*-
# flake8: noqa
"""
A Python library for FilePreview's API.
"""

__title__ = "filepreviews"
__version__ = "3.0.0rc1"
__author__ = "José Padilla"
__license__ = "MIT"
__copyright__ = "Copyright 2015 Blimp LLC"


VERSION = __version__
API_URL = "https://api.filepreviews.io/v2"

from .api import FilePreviews
from .exceptions import (
    APIError,
    AuthenticationError,
    FilePreviewsError,
    InvalidRequestError,
)

__all__ = [
    "FilePreviews",
    "FilePreviewsError",
    "APIError",
    "InvalidRequestError",
    "AuthenticationError",
]
