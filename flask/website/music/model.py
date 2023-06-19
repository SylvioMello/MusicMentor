import pandas as pd
import numpy as np
from numpy.linalg import norm

class TrackRecommender:
    def __init__(self, sp):
        self.sp = sp

    def recommend(self, track_id, data, n_recs=5, variables_to_dist=None):
        if variables_to_dist is None:
            variables_to_dist = ["valence", "energy"]

        data["mood_vec"] = data[variables_to_dist].values.tolist()

        track_features = self.sp.track_audio_features(track_id)
        track_moodvec = np.array([getattr(track_features, attr) for attr in variables_to_dist])

        data["distances"] = data["mood_vec"].apply(lambda x: norm(track_moodvec - np.array(x)))
        data_sorted = data.sort_values(by="distances", ascending=True)
        data_sorted = data_sorted[data_sorted["id"] != track_id]
        
        return data_sorted.iloc[:n_recs]
    
    @staticmethod
    def get_id_from_link(url):
        url = url.split('track/')[-1]
        return url

    @staticmethod
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