import os
import json
import requests
import datetime
from subprocess import Popen, PIPE, DEVNULL

def create_access_token(request_url, request_method):
    return Popen(['node', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'accessToken.js'), request_url, request_method], stdout=PIPE, stderr=DEVNULL).communicate()[0].decode().strip()

def send_request(request_url, request_method, payload):

    date = datetime.datetime.now(datetime.timezone.utc)
    date = date.strftime("%a, %d %b %Y %H:%M:%S GMT")

    headers = {
        'Content-Type': 'application/json',
        'Authorization': create_access_token(request_url, request_method),
        'nep-organization': 'test-drive-d2525f33ae1741398399d',
        'Date': date,
        'Accept': 'application/json',
        'Accept-Language': 'en-us'
    }
    if (len(payload) != 0):
        payload = json.dumps(payload)
    response = requests.request(request_method, request_url, headers=headers, data=payload)
    return response

def create_item(item_id, item_name, description, price, seller_id):
    request_url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/"+item_id
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
                    },
                    {
                        "key": "seller",
                        "value": seller_id
                    }
                ]
            }
        ]
    }

    response = send_request(request_url, request_method, payload)
    while(response.status_code != 204):
        response = send_request(request_url, request_method, payload)
    # print(response)
    return


def get_item(item_id):
    request_url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/"+item_id
    request_method = "GET"

    response = send_request(request_url, request_method, {})
    while(response.status_code != 200):
        response = send_request(request_url, request_method, {})
    data = response.json()
    # print(data)

    description = data['shortDescription']['values'][0]['value']
    price = data['dynamicAttributes'][0]['attributes'][0]['value']
    name = data['dynamicAttributes'][0]["attributes"][1]['value']

    return name, description, price

def update_item(item_id, item_name, description, price):
    request_url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/" + item_id
    request_method = "GET"
    GET_response = send_request(request_url, request_method, {})
    response_dict = GET_response.json()

    response_dict['version'] += 1
    response_dict['shortDescription']['values'][0]['values'] = description
    response_dict['dynamicAttributes'][0]['attributes'][0]['value'] = price
    response_dict['dynamicAttributes'][0]['attributes'][1]['value'] = item_name
    request_method = "POST"
    POST_response = send_request(request_url, request_method, response_dict)
    print(POST_response.text)


def delete_item(item_id):
    request_url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/" + item_id
    request_method = "GET"

    GET_response = send_request(request_url, request_method, {})
    while (GET_response.status_code != 200):
        GET_response = send_request(request_url, request_method, {})
    response_dict = GET_response.json()

    payload = {
        'version': response_dict['version']+1,
        'shortDescription': {
            "values": [
                {
                    "locale": "en-US",
                    "value": response_dict['shortDescription']['values'][0]['value']
                }
            ]
        },
        'merchandiseCategory': {
            'nodeId': '1-846-188-450'
        },
        "status": "INACTIVE",
        "departmentId": "783497",
        "nonMerchandise": None,
        "dynamicAttributes": [
            {
                "type": "String",
                "attributes": [
                    {
                        "key": "name",
                        "value": response_dict['dynamicAttributes'][0]['attributes'][1]['value']
                    },
                    {
                        "key": "price",
                        "value": response_dict['dynamicAttributes'][0]['attributes'][0]['value']
                    },
                    {
                        "key": "seller",
                        "value": response_dict['dynamicAttributes'][0]['attributes'][2]['value']
                    }
                ]
            }
        ]

    }

    request_method = "PUT"
    PUT_response = send_request(request_url, request_method, payload)
    while(PUT_response.status_code != 204):
        PUT_response = send_request(request_url, request_method, payload)


def create_seller():
    request_url = "https://gateway-staging.ncrcloud.com/cdm/consumers"
    request_method = "POST"

    payload = {
        'profileUsername': "bobthebuilder33@smallbusiness.com",
        "firstName": "Bob",
        "lastName": "the Builder",
        "effectiveDate": "2021-10-25",
        "gender": "Male",
        "phone": "4085671266",
        "mobile": "4081234599",
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

    response = send_request(request_url, request_method, payload)
    while(response.status_code != 200):
        response = send_request(request_url, request_method, payload)
    data = response.json()

    # put consumer id into database connecting to user
    consumer_id = data['consumerAccountNumber']
    return consumer_id

def get_seller(consumer_account_number):
    request_url = "https://gateway-staging.ncrcloud.com/cdm/consumers"+consumer_account_number
    request_method = "GET"

    response = send_request(request_url, request_method, {})
    data = response.json()
    print(data)

    username = data['profileUsername']
    first_name = data['firstName']
    last_name = data['lastName']
    birthday = data['birthDate']
    phone = data['phone']
    mobile = data['mobile']

    return username, first_name, birthday, last_name, phone, mobile

def list_of_objects():
    request_url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/?itemStatus=ACTIVE"
    request_method = "GET"

    response = send_request(request_url, request_method, {})
    while(response.status_code != 200):
        response = send_request(request_url, request_method, {})
    data = response.json()['pageContent']

    all_objects = []

    for i in range(len(data)):
        item = {}
        item_id = data[i]["itemId"]["itemCode"]
        description = data[i]["shortDescription"]["value"]

        response = send_request("https://gateway-staging.ncrcloud.com/catalog/v2/items/"+item_id, "GET", {})
        while(response.status_code != 200):
            response = send_request("https://gateway-staging.ncrcloud.com/catalog/v2/items/" + item_id, "GET", {})
        response_data = response.json()
        # print(response_data)
        price = response_data['dynamicAttributes'][0]['attributes'][0]['value']
        name = response_data['dynamicAttributes'][0]["attributes"][1]['value']
        item['id'] = item_id
        item['description'] = description
        item['name'] = name
        item['price'] = price

        all_objects.append(item)

    return all_objects

# def search_items_criteria(name):

# print(create_access_token("https://gateway-staging.ncrcloud.com/catalog/v2/items/itemObject", 'GET'))
# consumer_id = create_seller()
# print("Seller created with id {}".format(consumer_id))
# username, first_name, birthday, last_name, phone, mobile = get_seller("SAIA1XKMZ9R3IGXU")
# print("Seller {} {} retrieved".format(first_name, last_name))
# item_id = "11"
# create_item(item_id, "Ashish", "dumb but", "1", consumer_id)
# print("Item Ashish with id {} created with price 1".format(item_id))
# sleep(5)
# name, description, price = get_item(item_id)
# print("Item {} described as {} and price {} retrieved".format(name, description, price))
# print("All objects: \n")
# print(list_of_objects())
# delete_item(item_id)
# print("Item {} deleted".format(item_id))
# sleep(5)
# print("Now all objects are: \n")
# print(list_of_objects())
