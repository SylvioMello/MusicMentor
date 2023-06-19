import os
import pandas as pd
from flask import Blueprint, render_template, request, flash
from dotenv import load_dotenv
from .music.auth import SpotifyAuthorization
from .music.model import TrackRecommender

# definimos os 'caminhos'
views = Blueprint('views', __name__)

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# página inicial
@views.route('/', methods=['GET', 'POST'])
def home():
    track_id = None
    sp = SpotifyAuthorization(CLIENT_ID, CLIENT_SECRET).authorize()

    if request.method == 'POST':
        track_id = request.form.get('track_id')

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

        data = pd.read_csv('https://raw.githubusercontent.com/SylvioMello/MusicMentor/main/flask/website/music/spotify_data/data.csv')
        recommender = TrackRecommender(sp)
        recommendations = recommender.recommend(track_id, data, variables_to_dist = variables_to_dist)['id'].values.tolist()
        rec_links = []

        for rec_id in recommendations:
            rec_link = f"https://open.spotify.com/embed/track/{rec_id}?utm_source=generator"
            rec_links.append(rec_link)
        

        return render_template('base.html', your_song=link, recommendations_links=rec_links)
    
    return render_template('base.html')