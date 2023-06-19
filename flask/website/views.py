from flask import Blueprint, render_template, request, flash
import pandas as pd
from .music.auth import authorize
from .music.model import recommend
from .music.preproc import get_id_from_link, get_id_from_name

# definimos os 'caminhos'
views = Blueprint('views', __name__)

# página inicial
@views.route('/', methods=['GET', 'POST'])
def home():
    track_id = None
    sp = authorize()
    if request.method == 'POST':

        track_id = request.form.get('track_id')

        if 'spotify.com' in track_id:
            track_id = get_id_from_link(track_id) #track_id.split('/')[-1]
        else:
            try: 
                sp.track(track_id)
            except:
                try:
                    track_id = get_id_from_name(track_id)
                    sp.track(track_id)
                except:
                    flash('Invalid track ID. Please try again.', category='error')
                    return render_template('base.html')


        variables_to_dist = list(request.form)
        variables_to_dist.remove('track_id')
    

    
        link = f"https://open.spotify.com/embed/track/{track_id}?utm_source=generator"

        data = pd.read_csv('https://raw.githubusercontent.com/SylvioMello/MusicMentor/main/flask/website/music/spotify_data/data.csv')
        recommendations = recommend(track_id, data, sp, variables_to_dist = variables_to_dist)['id'].values.tolist()
        rec_links = []

        for rec_id in recommendations:
            rec_link = f"https://open.spotify.com/embed/track/{rec_id}?utm_source=generator"
            rec_links.append(rec_link)
        

        return render_template('base.html', your_song=link, recommendations_links=rec_links)
    
    return render_template('base.html')