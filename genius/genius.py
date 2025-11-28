import requests
import json

apikey = open('genius/.apikey')

blingingLights = requests.get(
    url="https://api.genius.com/songs/5049949?text_format=markdown",
    headers= {
        "Authorization" : f"Bearer {apikey}"
    }
)

open('response.json', 'w').write(json.dumps(blingingLights.json(), indent=4))