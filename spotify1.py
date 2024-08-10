import requests as rq
import json
import openai
def spotify(typ):  
        headers={
        "Authorization":"Bearer key",
        "Accept":"application/json",
        "Content-Type": "application/json"
        }
        searcher=rq.get(f"https://api.spotify.com/v1/search?q={typ}&type=playlist&limit=1&country=US",headers=headers)
        namea=searcher.json()
        playlist_id=namea['playlists']['items'][0]['id']
        playlists=rq.get(f'https://api.spotify.com/v1/playlists/{playlist_id}?q=limit=2&country=US',headers=headers)
        link=playlists.json()
        print(link["external_urls"]["spotify"])