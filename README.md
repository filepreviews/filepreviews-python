# FilePreviews.io
Python client library and CLI tool for the **Demo API** of [FilePreviews.io](http://filepreviews.io) service. Generate image previews and metadata from almost any kind of file. A lot more to come very soon.

[Sign up to beta](http://eepurl.com/To0U1)

## Installation

Using pip:
```
$ pip install filepreviews
```

Using easy_install:
```
$ easy_install filepreviews
````

## Usage
```python
>>> from filepreviews import FilePreviews
>>> fp = FilePreviews()
>>> fp.generate('http://www.getblimp.com/images/screenshot1.png')
{'preview_url': 'http://demo.filepreviews.io.s3-website-us-east-1.amazonaws.com/ea67bc0428d3c55fef53806482d21950699791dc4d713f7ea5567fc82848caee/screenshot1_original_1.png', 'metadata': {u'extra_data': {u'ocr': [{u'text': u'o\n-a\n5\nca\n:2\nre\n:1\n:2\nn\na\n\n...s.-. vvcwwy\n..._...n........_m..._-\n\n............... .0.-\n\na..........-..\u2014........\n._n.._...............\n\n \n\n', u'page': 1}], u'exif': {}}, u'thumbnails': [{u'url': u'https://s3.amazonaws.com/demo.filepreviews.io/ea67bc0428d3c55fef53806482d21950699791dc4d713f7ea5567fc82848caee/screenshot1_original_1.png', u'resized': False, u'total_pages': 1, u'original_size': {u'width': u'560', u'height': u'397'}, u'page': 1, u'size': {u'width': u'560', u'height': u'397'}}, {u'url': u'https://s3.amazonaws.com/demo.filepreviews.io/ea67bc0428d3c55fef53806482d21950699791dc4d713f7ea5567fc82848caee/screenshot1_1_1.png', u'resized': True, u'total_pages': 1, u'original_size': {u'width': u'560', u'height': u'397'}, u'page': 1, u'size': {u'width': u'1', u'height': u'1'}}]}}
```

### CLI
```
$ filepreviews http://www.getblimp.com/images/screenshot1.png
{"preview_url": "http://demo.filepreviews.io.s3-website-us-east-1.amazonaws.com/ea67bc0428d3c55fef53806482d21950699791dc4d713f7ea5567fc82848caee/screenshot1_original_1.png", "metadata": {"extra_data": {"ocr": [{"text": "o\n-a\n5\nca\n:2\nre\n:1\n:2\nn\na\n\n...s.-. vvcwwy\n..._...n........_m..._-\n\n............... .0.-\n\na..........-..\u2014........\n._n.._...............\n\n \n\n", "page": 1}], "exif": {}}, "thumbnails": [{"url": "https://s3.amazonaws.com/demo.filepreviews.io/ea67bc0428d3c55fef53806482d21950699791dc4d713f7ea5567fc82848caee/screenshot1_original_1.png", "resized": false, "total_pages": 1, "original_size": {"width": "560", "height": "397"}, "page": 1, "size": {"width": "560", "height": "397"}}, {"url": "https://s3.amazonaws.com/demo.filepreviews.io/ea67bc0428d3c55fef53806482d21950699791dc4d713f7ea5567fc82848caee/screenshot1_1_1.png", "resized": true, "total_pages": 1, "original_size": {"width": "560", "height": "397"}, "page": 1, "size": {"width": "1", "height": "1"}}]}}
```

## Build
```
git clone https://github.com/GetBlimp/filepreviews.js.git
cd filepreviews.js
npm install && grunt
```