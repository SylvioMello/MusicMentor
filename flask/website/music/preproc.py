import pandas as pd
from .auth import authorize

def get_id_from_link(url):
    url = url.split('track/')[-1]

    return url

def get_id_from_name(track_id_name):
    # dataset = pd.read_csv('dataset.csv')
    # dataset_indexed = dataset.set_index('name')
    # dataset_dict = dataset_indexed['id'].to_dict()

    try:
        track_id_name, track_id_artist = track_id_name.split(' - ')

        results = authorize().search(query=f"{track_id_name} artists:{track_id_artist}", types=['track'])
        for i in range(len(results[0].items)):
            if results[0].items[i].artists[-1].name.lower() == track_id_artist.lower():
                #print(results[0].items[i].id)

                return results[0].items[0].id
    except Exception as e:
        print(e)
        return None
    #return dataset_dict[track_id_name]




