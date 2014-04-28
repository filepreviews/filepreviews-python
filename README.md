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
$ filepreviews https://www.filepicker.io/api/file/0ehaqJwCTSq4P6jMrix6
{
    "preview_url": "https://s3.amazonaws.com/demo.filepreviews.io/a2b3e2beca03eece273e419a5e627823193c375bcb6817aa266d323a291acc5c/0ehaqJwCTSq4P6jMrix6_original_1.png",
    "metadata": {
        {
            "extra_data": {
                "ocr": [{
                    "page": 1,
                    "text": "Pebble\nE-Paper Watch for iPhone and Android\n\n1 4 1\n4\n1\n\n1\n\n2\n\n5\n\n3\n\n6\n\n1\n\nButton A\n\n4\n\nButton B\n\n2\n\nDisplay\n\n5\n\nButton C\n\n3\n\nCharge Port\n\n6\n\nButton D\n\nVersion 1.0\n\nPebble Technology, Corp\nPage 1 of 4\n\nNov 29, 2012\n\n\f"
                }, {
                    "page": 2,
                    "text": "Pebble\nE-Paper Watch for iPhone and Android\nCertiﬁcations and Safety Approvals\n• FCC Compliance Statement\nThis device complies with Part 15 of the FCC Rules. Operation is subject to the\nfollowing two conditions: (1) this device may not cause harmful interference, and (2) this\ndevice must accept any interference received, including interference that may cause\nundesired operation.\nCAUTION: Change or modification not expressly approved by the party responsible\nfor compliance could void the user’s authority to operate this equipment.\nThis equipment has been tested and found to comply with the limits for a Class B\ndigital device, pursuant to Part 15 of the FCC Rules. These limits are designed to\nprovide reasonable protection against harmful interference in a residential installation.\nThis equipment generates, uses and can radiate radio frequency energy and, if not\ninstalled and used in accordance with the instructions, may cause harmful interference\nto radio communications. However, there is no guarantee that interference will not occur\nin a particular installation. If this equipment does cause harmful interference to radio or\ntelevision reception, which can be determined by turning the equipment off and on, the\nuser is encouraged to try to correct the interference by one or more of the following\nmeasures:\n--Reorient or relocate the receiving antenna.\n--Increase the separation between the equipment and receiver.\n--Connect the equipment into an outlet on a circuit different from that to which the\nreceiver is connected.\n--Consult the dealer or an experienced radio/TV technician for help.\nCAUTION:\nAny changes or modifications not expressly approved by the grantee of this device\ncould\nvoid the user's authority to operate the equipment.\nRF exposure warning\nThis equipment must be installed and operated in accordance with provided instructions\nand the antenna(s) used for this transmitter must be installed to provide a separation\ndistance of at least 2.5 cm from all persons and must not be co-located or operating in\nconjunction with any other antenna or transmitter. End-users and installers must be\nprovide with antenna installation instructions and transmitter operating conditions for\nsatisfying RF exposure compliance.\"\n\nVersion 1.0\n\nPebble Technology, Corp\nPage 2 of 4\n\nNov 29, 2012\n\n\f"
                }, {
                    "page": 3,
                    "text": "\f"
                }, {
                    "page": 4,
                    "text": "Pebble\nE-Paper Watch for iPhone and Android\nWarranty\nFor more information on about the One Year Limited Warranty, please visit\nwww.getpebble.com/warranty.\n\nQuickstart Guide\nEach Pebble shipment includes:\n-One Pebble smartwatch\n-One Pebble USB charge cable\n• Charge Pebble\nAttach the curved end of the Pebble USB charge cable onto Pebble. Plug the other end\nof the cable into a USB port on a computer, laptop or USB wall charger.\nTo obtain a full charge, leave Pebble connected for at least 2 hours.\n• Download smartphone app\nPebble is compatible with the following iOS devices running at least iOS 5 or greater:\n-iPhone 3GS\n-iPhone 4\n-iPhone 4S\n-iPhone 5\n-iPod Touch 3rd to 5th generation\nPebble is compatible with Android smartphones running Android OS 2.3.3 or higher.\nDownload the Pebble App by visiting http://go.getpebble.com from the iOS or Android\nbrowser.\n• Bluetooth pairing\nEnable Bluetooth in iOS or Android settings. Perform a Bluetooth device scan. Pebble\nwill show up with the name “Pebble XXXX” where XXXX is a unique identi ﬁer (the last 4\ndigits of the serial number imprinted on the back of the watch). After selecting the ‘Pair’\noption, a conﬁrmation prompt will be presented on the watch display. Press Button C to\nconﬁrm the pairing. Then conﬁrm the pairing on the smartphone side.\n• Open Pebble App\nAfter installing the Pebble App and pairing via Bluetooth, open the Pebble App on iOS\nor Android. After each reboot, the Pebble App needs to be opened.\nVersion 1.0\n\nPebble Technology, Corp\nPage 4 of 4\n\nNov 29, 2012\n\n\f"
                }, {
                    "page": 5,
                    "text": "Pebble Bluetooth Watc\nForm Factor\n\nKey Features\n•\n\nST ARM 32-bit CORTEX –M3 CPU\n\n•\n\nPanasonic PAN1316 Bluetooth EDR 2.1 (4.0\ndisable) module support SPP, AVRCP profile;\nThe maximum power consumption is less\nthan 15 mA and the average power\nconsumption is about 1 uA\n\n•\n\nWaterproof to 5 ATM\n\n•\n\nAccelerometer and magnetometer sensor\n\n•\n\nVibrator indicate\n\n•\n\nDisplay Backlight\n\n•\n\nLiPoly Battery (120mAh)\n\n•\n\n•\n•\n\nDimension:\n50.33 mm X 32 m\nWeight: 39g\nOperation Syste\n\nSHARP 1.26’,TFT LCD module with 144 ×\n168 resolution in a 24192-pixel stripe array\n\n•\n\n•\n\n4 function Key\n\nID for referen\n2012/11/27\n\nMicrolink Confidential\n\n\f"
                }],
                "exif": {}
            },
            "thumbnails": [{
                "size": {
                    "width": "612",
                    "height": "792"
                },
                "url": "https://s3.amazonaws.com/demo.filepreviews.io/a2b3e2beca03eece273e419a5e627823193c375bcb6817aa266d323a291acc5c/0ehaqJwCTSq4P6jMrix6_original_1.png",
                "page": 1,
                "resized": false,
                "original_size": {
                    "width": "612",
                    "height": "792"
                },
                "total_pages": 5
            }, {
                "size": {
                    "width": "612",
                    "height": "792"
                },
                "url": "https://s3.amazonaws.com/demo.filepreviews.io/a2b3e2beca03eece273e419a5e627823193c375bcb6817aa266d323a291acc5c/0ehaqJwCTSq4P6jMrix6_original_2.png",
                "page": 2,
                "resized": false,
                "original_size": {
                    "width": "612",
                    "height": "792"
                },
                "total_pages": 5
            }, {
                "size": {
                    "width": "612",
                    "height": "792"
                },
                "url": "https://s3.amazonaws.com/demo.filepreviews.io/a2b3e2beca03eece273e419a5e627823193c375bcb6817aa266d323a291acc5c/0ehaqJwCTSq4P6jMrix6_original_3.png",
                "page": 3,
                "resized": false,
                "original_size": {
                    "width": "612",
                    "height": "792"
                },
                "total_pages": 5
            }, {
                "size": {
                    "width": "612",
                    "height": "792"
                },
                "url": "https://s3.amazonaws.com/demo.filepreviews.io/a2b3e2beca03eece273e419a5e627823193c375bcb6817aa266d323a291acc5c/0ehaqJwCTSq4P6jMrix6_original_4.png",
                "page": 4,
                "resized": false,
                "original_size": {
                    "width": "612",
                    "height": "792"
                },
                "total_pages": 5
            }, {
                "size": {
                    "width": "612",
                    "height": "792"
                },
                "url": "https://s3.amazonaws.com/demo.filepreviews.io/a2b3e2beca03eece273e419a5e627823193c375bcb6817aa266d323a291acc5c/0ehaqJwCTSq4P6jMrix6_original_5.png",
                "page": 5,
                "resized": false,
                "original_size": {
                    "width": "612",
                    "height": "792"
                },
                "total_pages": 5
            }]
        }
    }
}
```