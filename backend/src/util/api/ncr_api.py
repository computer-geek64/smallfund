import os
import json
import hmac
import base64
import hashlib
import requests
from subprocess import Popen, PIPE, DEVNULL


def calculateSignature():
    stringToSign = "Test"
    secretAccessKey = "bAvW5O18eSrxke4I7eFcrnrDJkN+wKQmx9aSHuMZQ0w="

    secretAccessKeyBase64 = base64.b64decode(secretAccessKey)
    keyBytes = secretAccessKeyBase64
    stringToSignBytes = bytes(stringToSign, 'utf-8')

    signatureHash = hmac.new(keyBytes, stringToSignBytes, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(signatureHash)
    print(signature)


def create_access_token(request_url, request_method):
    return Popen(['/usr/bin/node', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'accessToken.js'), request_url, request_method], stdout=PIPE, stderr=DEVNULL).communicate()[0].decode()


def create_item(item_id, item_name, description, price):
    url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/"+item_id
    request_method = "PUT"

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
        'Authorization': create_access_token(url, request_method),
        'nep-organization': 'test-drive-d2525f33ae1741398399d',
        'Date': 'Sat, 23 Oct 2021 21:20:30 GMT',
        'Accept': 'application/json',
        'Accept-Language': 'en-us'
    }

    response = requests.request(request_method, url, headers=headers, data=payload)
    print(response)


def get_item(item_id):
    url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/"+item_id
    request_method = "GET"

    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': create_access_token(url, request_method),
        'nep-organization': 'test-drive-d2525f33ae1741398399d',
        'Date': 'Sat, 23 Oct 2021 21:20:30 GMT',
        'Accept': 'application/json',
        'Accept-Language': 'en-us'
    }

    response = requests.request(request_method, url, headers=headers, data=payload)

    print(response.text)

def update_item(item_id, item_name, description, price):
    url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/" + item_id
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'AccessKey 8a4914a9f08b4a45916012763aafe24a:mofshVcVG86ew0wO4dZuWI661la5tm6Lam97qd9PpyyrAibEJTch1D38Op0rgdGrxIBdRHFEJSO0wXC6BxJ5oA==',
        'nep-organization': 'test-drive-d2525f33ae1741398399d',
        'Date': 'Sat, 23 Oct 2021 21:20:30 GMT',
        'Accept': 'application/json',
        'Accept-Language': 'en-us'
    }
    GET_response = requests.request("GET", url, headers=headers, data=payload)
    response_dict = json.loads(GET_response)

    response_dict['version'] += 1
    response_dict['shortDescription']['values'][0]['values'] = description
    response_dict['dynamicAttributes'][0]['attributes'][0]['value'] = price
    response_dict['dynamicAttributes'][0]['attributes'][1]['value'] = item_name
    POST_response = requests.request("PUT", url, headers=headers, data=response_dict)
    print(POST_response.text)



# def delete_item(item_name):
#
#

def create_seller():
    url = "https://gateway-staging.ncrcloud.com/cdm/consumers"
    request_method = "POST"

    payload = {
        "profileUsername": "bobthebuilder@smallbusiness.com",
        "firstName": "Bob",
        "lastName": "the Builder",
        "effectiveDate": "2021-10-25",
        "gender": "Male",
        "phone": "4085671234",
        "mobile": "4081234567",
        "addresses": [
            {
                "name": "Office",
                "line1": "864 Spring St NW",
                "line2": "North Tower. 14th Floor",
                "city": "Atlanta",
                "state": "GA",
                "postalCode": "30308",
                "country": "USA"
            }
        ]
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': create_access_token(url, request_method),
        'nep-organization': 'test-drive-d2525f33ae1741398399d',
        'Date': 'Sat, 23 Oct 2021 21:20:30 GMT',
        'Accept': 'application/json',
        'Accept-Language': 'en-us'
    }

    response = requests.request(request_method, url, headers=headers, data=payload)
    data = response.json()

    # put consumer id into database connecting to user
    consumer_id = data['consumerAccountNumber']
    return consumer_id

# def search_items_criteria(name):

print(create_access_token("https://gateway-staging.ncrcloud.com/catalog/v2/items/1", 'PUT'))