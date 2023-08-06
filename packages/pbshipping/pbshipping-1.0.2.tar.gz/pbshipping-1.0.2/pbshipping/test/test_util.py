#
# Copyright 2016 Pitney Bowes Inc.
# Licensed under the MIT License (the "License"); you may not use this file 
# except in compliance with the License.  You may obtain a copy of the License 
# in the LICENSE file or at 
#
#    https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and 
# limitations under the License.
#
# File: shipment_test.py
# Description: supporting classes for test suite
#

import time
import os

_test_api_key=None # <set here or through env variable PBSHIIPING_KEY"
_test_api_secret=None # <set here or through env variable PBSHIPPING_SECRET"
_test_devid=None # <set here or through env variable PBSHIPPING_DEVID"
_test_merchant_email=None # <set here or through env variable PBSHIPPING_MERCHNAT"

_MY_BULK_MERCHANT_ADDR = {
    "addressLines" : ["27 Waterview Drive"], 
    "cityTown" : "Shelton",
    "stateProvince" : "Connecticut",
    "postalCode" : "06484",
    "countryCode" : "US",
    "company" : "Pitney Bowes",
    "name": "John Doe",
    "email" : "dummy@pbshipping.com", 
    "phone": "203-792-1600",
    "residential": False
}

_MY_ORIGIN_ADDR = {
    "addressLines" : ["37 Executive Drive"], 
    "cityTown" : "Danbury",
    "stateProvince" : "Connecticut",
    "postalCode" : "06810",
    "countryCode" : "US"
}

_MY_DEST_ADDR = {
    "addressLines" : ["27 Waterview Drive"], 
    "cityTown" : "Shelton",
    "stateProvince" : "Connecticut",
    "postalCode" : "06484",
    "countryCode" : "US"
}
   
_MY_PARCEL = {
    "weight": {
        "unitOfMeasurement":"OZ",
        "weight":1
    },
    "dimension":{
        "unitOfMeasurement":"IN",
        "length":6,
        "width":0.25,
        "height":4,
        "irregularParcelGirth":0.002
    }
}

_MY_RATE_REQUEST_CARRIER_USPS = {
    "carrier":"usps",
    "serviceId":"PM",
    "parcelType":"PKG",
    "specialServices": [
        {
            "specialServiceId":"Ins",
            "inputParameters" : [
                {
                    "name" : "INPUT_VALUE",
                    "value" : "50"
                }
             ]
        },
        {
            "specialServiceId":"DelCon",
            "inputParameters" : [
                {
                    "name" : "INPUT_VALUE",
                    "value" : "0"
                }
             ]
        }
    ],
    "inductionPostalCode":"06484"
}

_MY_SHIPMENT_DOCUMENT = {
    "type": "SHIPPING_LABEL",
    "contentType": "URL",
    "size": "DOC_8X11",
    "fileFormat": "PDF",
    "printDialogOption": "NO_PRINT_DIALOG"
}

def setup_env():
    global _test_api_key, _test_api_secret, _test_devid, _test_merchant_email
    
    if _test_api_key is None:
        _test_api_key = os.environ.get("PBSHIPPING_KEY", None)
    if _test_api_secret is None:
        _test_api_secret = os.environ.get("PBSHIPPING_SECRET", None)
    if _test_devid is None:
        _test_devid = os.environ.get("PBSHIPPING_DEVID", None)
    if _test_merchant_email is None:
        _test_merchant_email = os.environ.get("PBSHIPPING_MERCHANT", None)  
    
def get_pb_tx_id():
    return str(int(time.time()))

