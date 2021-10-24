import hashlib
import hmac

import requests
import base64
import json

def calculateSignature():
    stringToSign = "Test"
    secretAccessKey = "bAvW5O18eSrxke4I7eFcrnrDJkN+wKQmx9aSHuMZQ0w="

    secretAccessKeyBase64 = base64.b64decode(secretAccessKey)
    keyBytes = secretAccessKeyBase64
    stringToSignBytes = bytes(stringToSign, 'utf-8')

    signatureHash = hmac.new(keyBytes, stringToSignBytes, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(signatureHash)
    print(signature)

def create_access_token(organization, shared_key, secret_key):
    regexPattern = / ({{(.* ?)}}) / g;

    signature = calculateSignature()
    access_key = 'AccessKey ' + shared_key + ':' + signature

def create_item(item_id, item_name, description, price):
    url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/"+item_id

    payload = {
        'version': 1,
        'shortDescription': {
            "values": [
                {
                    "locale": "en-US",
                    "value": description
                }
            ]
        },
        'merchandiseCategory': {
            'nodeId': '1-846-188-450'
        },
        "status": "ACTIVE",
        "departmentId": "783497",
        "nonMerchandise": None,
        "dynamicAttributes": [
            {
                "type": "String",
                "attributes": [
                    {
                        "key": "name",
                        "value": item_name
                    },
                    {
                        "key": "price",
                        "value": price
                    }
                ]
            }
        ]

    }


    payload = json.dumps(payload)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'AccessKey 8a4914a9f08b4a45916012763aafe24a:jEwPpu3n23NeYouXHnx8BjUM6AvV2fCvU+7nsbvwnJmA5XZM4OeMIleh/TM1Y388pu1Zw8eZCTpXbaDFIe7bpQ==',
        'nep-organization': 'test-drive-d2525f33ae1741398399d',
        'Date': 'Sat, 23 Oct 2021 21:20:30 GMT',
        'Accept': 'application/json',
        'Accept-Language': 'en-us'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response)

def get_item(item_id):
    url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/"+item_id

    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'AccessKey 8a4914a9f08b4a45916012763aafe24a:mofshVcVG86ew0wO4dZuWI661la5tm6Lam97qd9PpyyrAibEJTch1D38Op0rgdGrxIBdRHFEJSO0wXC6BxJ5oA==',
        'nep-organization': 'test-drive-d2525f33ae1741398399d',
        'Date': 'Sat, 23 Oct 2021 21:20:30 GMT',
        'Accept': 'application/json',
        'Accept-Language': 'en-us'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

# def update_item(item_name):
#
#
# def delete_item(item_name):
#
#
# def create_seller(name):
#
#
# def search_items_criteria(name):

create_item("1", "spatula", "a kitchen tool", "30")
