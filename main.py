from youtubesearchpython import *
import urllib.request
import pandas as pd
import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_track_link(song_name, artist_name):
    # Enter your Spotify API credentials
    client_id = 'f350939af76d45208d401bbf766efee8'
    client_secret = '5262f0351bef497d9563b3248371fb4f'

    # Create a Spotify API client
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Search for the track using the song and artist names
    query = f'track:{song_name} artist:{artist_name}'
    results = sp.search(q=query, limit=1, type='track')

    # Extract the Spotify track link from the search results
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_link = track['external_urls']['spotify']
        return track_link

    return None
def get_spotify_views(song_link,song_name):
    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        try:
            r = requests.get(song_link)
            r.raise_for_status()  # Raises an exception for non-2xx status codes
            break  # Break out of the loop if the request is successful
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
            retry_count += 1
            print(f"Retrying... (attempt {retry_count} of {max_retries})")

    if retry_count == max_retries:
        print("Max retry attempts reached. Exiting.")
    else:
        print("Request successful")

    soup = BeautifulSoup(r.content,'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib
    spans = soup.find_all('span', {'class': 'ListRowTitle__LineClamp-sc-1xe2if1-0 doJkPH'})
    songs = [span.get_text() for span in spans]
    spans = soup.find_all('span', {'class': 'ListRowDetails__LineClamp-sc-sozu4l-0 xQfpa'})
    views = [span.get_text() for span in spans]
    index = 0
    song_name = song_name.split()
    for song in songs:
        if song_name[0] in song:
            return views[index]
        index = index + 1
    return None

def get_youtube_views(song_link):
    video = Video.get(song_link, mode=ResultMode.json, get_upload_date=True)
    return video["viewCount"]["text"]

def get_anghami_views(song_link):
    if type(song_link) == str:
        fp = urllib.request.urlopen(song_link)
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        fp.close()
        st = mystr.find("Plays")
        temp_str = 'abcdefghijlmnopqrstuvwxyz<>""'
        mystr = mystr[st - 37:st - 29]
        for i in mystr:
            if i in temp_str:
                mystr = mystr.replace(i, "")
        if mystr == "&;:":
            return None
        else:
            return mystr
    else:
        return None

count =0
if __name__=="__main__":
    df = pd.read_excel(r"C:\Users\minha\PycharmProjects\SongsData\youtubeviews.xlsx")
    df1 = pd.read_excel(r"C:\Users\minha\PycharmProjects\SongsData\songs.xlsx")
    video_views = []
    #spotipy_views = []
    count = 0
    find = 0
    nfind = 0
    for index, row in df.iterrows():
        song_name = row["Song Name"]
        artist_name = row["Artist Name"]
        youtube_link = row["Youtube link"]
        anghami_link = row["Anghami Link"]
        song_link = row["Spotify Link"]
    for index, row in df1.iterrows():
        spotipy_views = row["Spotify streams"]
        #print(type(spotipy_views))
        if type(spotipy_views) == str:
            find = find +1
        else:
            nfind=nfind+1
        #video_views.append(get_youtube_views(youtube_link))
        #anghami_views.append(get_anghami_views(anghami_link))
        #if type(song_link) == str:
           # spotipy_views.append(get_spotify_views(song_link,song_name))
      # else:
           # spotipy_views.append(None)

        #print(anghami_link, "  ", anghami_views[count])
        #print(song_name," ",spotipy_views[count])
        #count = count+1
    print("Found",find,"NFound",nfind)
    df1["Spotify streams"] = spotipy_views
    print(df1)
    #df1["YouTube views"] = video_views
    #df1.to_excel("songs.xlsx",index=False)