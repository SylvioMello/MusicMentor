import os
import pandas as pd
from flask import Blueprint, render_template, request, flash
from dotenv import load_dotenv
from .music.auth import SpotifyAuthorization
from .music.model import TrackRecommender

# Definimos os caminhos
views = Blueprint('views', __name__)

# Obtendo credenciais
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Página inicial
@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return process_post_request()
    
    return render_template('base.html')

def process_post_request():
    track_id = request.form.get('track_id')
    sp = authorize_spotify()

    if 'spotify.com' in track_id:
        track_id = TrackRecommender.get_id_from_link(track_id)
    else:
        try: 
            sp.track(track_id)
        except:
            try:
                track_id = TrackRecommender.get_id_from_name(track_id)
                sp.track(track_id)
            except:
                flash('Invalid track ID. Please try again.', category='error')
                return render_template('base.html')

    variables_to_dist = list(request.form)
    variables_to_dist.remove('track_id')

    link = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator"
    data = load_data_from_csv()
    recommender = create_recommender(sp)
    recommendations = recommender.recommend(track_id, data, variables_to_dist=variables_to_dist)['id'].values.tolist()
    rec_links = generate_recommendation_links(recommendations)

    return render_template('base.html', your_song=link, recommendations_links=rec_links)

def authorize_spotify():
    return SpotifyAuthorization(CLIENT_ID, CLIENT_SECRET).authorize()

def load_data_from_csv():
    return pd.read_csv('https://raw.githubusercontent.com/SylvioMello/MusicMentor/main/flask/website/music/spotify_data/data.csv')

def create_recommender(sp):
    return TrackRecommender(sp)

def generate_recommendation_links(recommendations):
    rec_links = []
    for rec_id in recommendations:
        rec_link = f"https://open.spotify.com/embed/track/{rec_id}?utm_source=generator"
        rec_links.append(rec_link)
    return rec_links
