#connect to nexus cliapi
#body taken from Postman / nxapi tool
import requests 
import json 

url = "https://sbx-nxos-mgmt.cisco.com:443/ins" 
username = "admin"
password = "Admin_1234!"

headers = {"Content-Type":"application/json"} 

payload = { 
    "ins_api": { 
        "version": "1.0", 
        "type": "cli_show", 
        "chunk": "0", 
        "sid": "sid", 
        "input": "show ip interface brief", 
        "output_format": "json" 
        } 
    }

response = requests.post(url, headers=headers,auth=(username,password), data=json.dumps(payload), verify=False).json()

print(json.dumps(response, indent=2, sort_keys=True))