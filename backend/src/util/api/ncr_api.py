import requests
import base64

def create_item(item_id, item_name, description, price):
    url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/"+item_id

    payload = "{\n    \"version\": 1,\n    \"packageIdentifiers\": [\n        {\n            \"type\": \"Type_1\",\n            \"value\": \"value_1\"\n        }\n    ],\n    \"longDescription\": {\n        \"values\": [\n            {\n                \"locale\": \"en-US\",\n                \"value\": \"Sample text in American English\"\n            },\n            {\n                \"locale\": \"fr-ca\",\n                \"value\": \"Sample text in French Canadian\"\n            },\n            {\n                \"locale\": \"en-br\",\n              \"value\": \"Sample text in American English\"\n            }\n        ]\n    },\n    \"shortDescription\": {\n        \"values\": [\n            {\n                \"locale\": \"en-US\",\n                \"value\": \"Sample text in American English\"\n            },\n            {\n                \"locale\": \"fr-ca\",\n                \"value\": \"Sample text in French Canadian\"\n            },\n            {\n                \"locale\": \"en-br\",\n                \"value\": \"Sample text in American English\"\n            }\n        ]\n    },\n    \"merchandiseCategory\": {\n        \"nodeId\": \"1-846-188-450\"\n    },\n    \"alternateCategories\": [\n        {\n            \"nodeId\": \"1-846-188-450\"\n        }\n    ],\n    \"status\": \"ACTIVE\",\n    \"departmentId\": \"783497\",\n    \"nonMerchandise\": null,\n    \"familyCode\": \"732897\",\n    \"referenceId\": \"832022\",\n    \"manufacturerCode\": \"46743234\",\n    \"externalIdentifiers\": [\n        {\n            \"type\": \"NACS_CODE\",\n            \"value\": \"3031\"\n        }\n    ],\n    \"posNumber\": \"String\",\n    \"dynamicAttributes\": [\n        {\n            \"type\": \"String\",\n            \"attributes\": [\n                {\n                    \"key\": \"key\",\n                    \"value\": \"value\",\n                    \"localizedValue\": {\n                        \"values\": [\n                            {\n                                \"locale\": \"en-US\",\n                                \"value\": \"sample text\"\n                            },\n                            {\n                                \"locale\": \"fr-ca\",\n                                \"value\": \"Sample text in French Canadian\"\n                            }\n                        ]\n                    }\n                }\n            ]\n        }\n    ]\n}"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'AccessKey 8a4914a9f08b4a45916012763aafe24a:mofshVcVG86ew0wO4dZuWI661la5tm6Lam97qd9PpyyrAibEJTch1D38Op0rgdGrxIBdRHFEJSO0wXC6BxJ5oA==',
        'nep-organization': 'test-drive-d2525f33ae1741398399d',
        'Date': 'Sat, 23 Oct 2021 21:20:30 GMT',
        'Accept': 'application/json',
        'Accept-Language': 'en-us'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

def get_item(item_name):
    url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/"+item_name

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

def update_item(item_name):


def delete_item(item_name):


def create_seller(name):


def search_items_criteria(name):


