from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_USERNAME = os.getenv("SPOTIPY_USERNAME")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")


def web_scrap_songs_data():
    string_date = input("From which date top 100 songs you wanna get? (YYYY-MM-DD)")
    base_url = "https://www.billboard.com/charts/hot-100/"
    response = requests.get(base_url + string_date)
    response.raise_for_status()
    website_html = response.text
    soup = BeautifulSoup(website_html, "html.parser")
    songs = soup.select("li ul li h3")
    songs_titles = [song.getText().strip() for song in songs]
    artists = soup.select("li ul li.o-chart-results-list__item span.c-label.a-font-primary-s")
    artists_names = [artist.getText().strip() for artist in artists]
    songs_data = [{'title': title, 'artist': artist} for title, artist in zip(songs_titles, artists_names)]
    return songs_data


def spotipy_auth():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private",  # Add the necessary scopes (e.g., "user-library-read")
        show_dialog=True,
        cache_path="token.txt"
    ))
    return sp


def generate_spotify_playlist():
    songs_data = web_scrap_songs_data()
    sp = spotipy_auth()
    user_id = sp.current_user()["id"]
    # Get the playlist ID
    playlist_name = input("Enter your playlist name:")
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    playlist_id = playlist['id']

    # Search for each song and add it to the playlist
    for song_data in songs_data:
        title = song_data['title']
        artist = song_data['artist'].split(" ")[0]
        results = sp.search(q=f"{title} artist:{artist}", type='track')

        # Check if any results are returned
        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.playlist_add_items(playlist_id, [track_uri])
            print(f"Added {title} to the playlist.")
        else:
            print(f"Could not find {title} by {artist} on Spotify.")


if __name__ == "__main__":
    generate_spotify_playlist()
