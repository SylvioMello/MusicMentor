import pandas as pd
import numpy as np
from numpy.linalg import norm


def recommend(track_id, data, sp, n_recs = 5, variables_to_dist = []):
    if variables_to_dist == []:
        variables_to_dist = ["valence", "energy"]

    data["mood_vec"] = data[variables_to_dist].values.tolist()

    track_features = sp.track_audio_features(track_id)
    #track_moodvec = np.array([track_features.valence, track_features.energy])
    track_moodvec = np.array([getattr(track_features, attr) for attr in variables_to_dist])


    # Compute distances to all reference tracks
    data["distances"] = data["mood_vec"].apply(lambda x: norm(track_moodvec-np.array(x)))
    # Sort distances from lowest to highest
    data_sorted = data.sort_values(by = "distances", ascending = True)
    # If the input track is in the reference set, it will have a distance of 0, but should not be recommendet
    data_sorted = data_sorted[data_sorted["id"] != track_id]
    (data_sorted.columns)

    # Return n recommendations
    return data_sorted.iloc[:n_recs]