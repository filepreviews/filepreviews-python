FilePreviews.io
===============

|Build Status|
|PyPI Status|

Python client library and CLI tool for the `FilePreviews.io`_ service. Generate image previews and metadata from almost any kind of file.

Installation
------------

Using pip:

::

    $ pip install filepreviews

Using easy\_install:

::

    $ easy_install filepreviews

Usage
-----

.. code:: python

    >>> from filepreviews import FilePreviews
    >>> fp = FilePreviews(api_key='API_KEY_HERE', api_secret='API_SECRET_HERE')
    >>> fp.generate('http://www.getblimp.com/images/screenshot1.png')
    <PreviewResult at 4497022216> JSON: {
      "id": "220214ec-17ec-4f37-a790-eaea64522bf2",
      "original_file": null,
      "preview": null,
      "status": "pending",
      "thumbnails": null,
      "url": "https://api.filepreviews.io/v2/previews/220214ec-17ec-4f37-a790-eaea64522bf2/",
      "user_data": null
    }

CLI
~~~

::

    $ filepreviews \
        --api_key=API_KEY_HERE \
        --api_secret=API_SECRET_HERE \
        generate http://www.getblimp.com/images/screenshot1.png
    {
      "id": "e48c645d-8c02-40ab-9f11-2b3f2316be15",
      "original_file": null,
      "preview": null,
      "status": "pending",
      "thumbnails": null,
      "url": "https://api.filepreviews.io/v2/previews/e48c645d-8c02-40ab-9f11-2b3f2316be15/",
      "user_data": null
    }

::

    $ filepreviews \
        --api_key=API_KEY_HERE \
        --api_secret=API_SECRET_HERE \
        retrieve e48c645d-8c02-40ab-9f11-2b3f2316be15
    {
      "id": "e48c645d-8c02-40ab-9f11-2b3f2316be15",
      "original_file": null,
      "preview": null,
      "status": "pending",
      "thumbnails": null,
      "url": "https://api.filepreviews.io/v2/previews/e48c645d-8c02-40ab-9f11-2b3f2316be15/",
      "user_data": null
    }

.. _FilePreviews.io: http://filepreviews.io
.. |Build Status| image:: https://travis-ci.org/GetBlimp/filepreviews-python.svg?branch=master
   :target: https://travis-ci.org/GetBlimp/filepreviews-python
.. |PyPI Status| image:: https://img.shields.io/pypi/v/filepreviews.svg
   :target: https://pypi.python.org/pypi/filepreviews
