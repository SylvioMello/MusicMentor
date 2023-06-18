import pandas as pd

def get_id_from_link(url):
    url = url.split('/')[-1]

    return get_id_from_link

def get_id_from_name(track_id_name):
    dataset = pd.read_csv('dataset.csv')
    dataset_indexed = dataset.set_index('name')
    dataset_dict = dataset_indexed['id'].to_dict()

    return dataset_dict[track_id_name]




