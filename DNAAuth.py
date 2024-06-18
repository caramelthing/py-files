#taken from my working postman environment

import requests
import json
username="devnetuser"
password="Cisco123!"

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload = {}
headers ={"Content-Type":"application/json"} 

response = requests.post(url, headers=headers,auth=(username,password), verify=False).json
print(json.dumps(response, indent=2, sort_keys=True))