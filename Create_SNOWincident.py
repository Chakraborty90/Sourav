import requests
import json

url = "https://dev147253.service-now.com/api/now/table/incident"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

Payload = {
    "short_description":"This is coming from python file."
}

res = requests.post(url, auth=("admin", "XXXX"), headers= headers, data = json.dumps(payload))

print(res.text)
