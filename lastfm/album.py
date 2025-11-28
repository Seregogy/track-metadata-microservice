import requests

class AlbumGetInfo:
    def __init__(self, name: str, artist: str, tags: list[str], description: str):
        self.name = name
        self.artist = artist
        self.tags = tags
        self.description = description

class LastFmAlbumFetcher:
    def __init__(self, apikey: str):
        self.apikey = apikey
    
    def getInfo(self, artist: str, album: str) -> AlbumGetInfo:
        response = requests.get(
            url="https://ws.audioscrobbler.com/2.0/",
            params={
                "method": "album.getInfo",
                "artist": artist,
                "album": album,
                "autocorrect": 1,
                "api_key": self.apikey,
                "format": "json"
            }
        ).json()["album"]

        return AlbumGetInfo(
            name=response["name"],
            artist=response["artist"],
            tags=[i["name"] for i in response["tags"]["tag"]],
            description=response["wiki"]["summary"]
        )
    
    def getTags(self, artist: str, album: str) -> list[str]:
        response = requests.get(
            url="https://ws.audioscrobbler.com/2.0/",
            params={
                "method": "album.getTopTags",
                "artist": artist,
                "album": album,
                "user": "RJ",
                "autocorrect": 1,
                "api_key": self.apikey,
                "format": "json"
            }
        ).json()

        print(response)

        return []