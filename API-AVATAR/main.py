import requests
import json

url = "https://last-airbender-api.fly.dev/api/v1/characters"

response = requests.get(url)

print(response.status_code)
print(json.dumps(response.json(), indent=4))