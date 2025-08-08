import requests
import json
def avatar_api ():
    url = "https://last-airbender-api.fly.dev/api/v1/characters"

    response = requests.get(url)

    return response
    