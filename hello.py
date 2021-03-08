from flask import Flask, render_template, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

app = Flask(__name__)



@app.route('/')
def hello_world():


    return render_template('authorization.html')



@app.route('/index')
def index():
    scope = "user-library-read, playlist-modify-public, user-top-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


    return render_template('index.html')


@app.route('/list')
def call():
    scope = "user-library-read, playlist-modify-public, playlist-modify-private"
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    me = sp.me()
    app_user_id = me['id']

    create_list_response = sp.user_playlist_create(app_user_id, "Test List", public=False, collaborative=False, description='Im making this for kev')

    results = sp.current_user_saved_tracks(50)
    items = results['items']
    # for idx, item in enumerate(results['items']):
    #     track = item['track']
    #     print(idx, track['artists'][0]['name'], " – ", track['name'])

    return render_template('list.html', results=results, items=items)

