from lastfm.album import *
import json

apikey = open('lastfm/.apikey').read()

albumFetcher = LastFmAlbumFetcher(apikey)
austin = albumFetcher.getInfo("Post Malone", "Austin")
print(austin.name)
print(austin.artist)
print(austin.description)
print(austin.tags)
print()

austinTags = albumFetcher.getTags("Post Malone", "Austin")

artist = "Juice WRLD"
track = "Robbery"
response = requests.get(f"https://ws.audioscrobbler.com/2.0/?method=track.gettoptags&artist={artist}&track={track}&api_key={apikey}&format=json")

print(json.dumps(response.json(), indent=4))