import requests
import json
from pprint import pprint

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "Admin_1234!"
    }
  }
})

headers = {
  'Content-Type': 'application/json'
  }

username = "admin"
password = "Admin_1234!"

response = requests.post(url, headers=headers, auth=(username, password),data=payload, verify=False).json()

token = response['imdata'][0]['aaaLogin']['attributes']['token']
#print(token)
cookies={}
cookies['APIC-cookie']=token
#not just parse through the python dictionary to [find][the][token], but actually create an empty dictionary and set a key called "APIC-cookie" = the newly parsed token
print(cookies)

