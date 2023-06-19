import pandas as pd

def get_id_from_link(url):
    url = url.split('track/')[-1]
    return url

def get_id_from_name(track_id_name, sp):
    try:
        track_id_name, track_id_artist = track_id_name.split(' - ')

        results = sp.search(query=f"{track_id_name} artists:{track_id_artist}", types=['track'])
        for i in range(len(results[0].items)):
            if results[0].items[i].artists[-1].name.lower() == track_id_artist.lower():
                return results[0].items[0].id
    except Exception as e:
        print(e)
        return None