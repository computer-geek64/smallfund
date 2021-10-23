import requests
import base64


def login(username, password):
    url = "https://gateway-staging.ncrcloud.com/security/authentication/login"
    decoded = f'{username}:{password}'
    encoded = base64.b64encode(decoded.encode()).decode("ISO-8859-1")

    headers = {
        'Authorization': f'Basic {encoded}'
    }

    response = requests.request("POST", url, headers=headers, data={})
    print(response)
    token = response.json()['token']

    return f'AccessToken {token}'

#login("acct:test-drive-d2525f33ae1741398399d@5115addc-be19-4b43-819e-4755c57dc5a1", "f3CS0adi^By*")


url = "https://gateway-staging.ncrcloud.com/catalog/v2/items/itemObject"

payload={}
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