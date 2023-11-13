Project README: Song Analytics

Overview:
This project focuses on collecting and analyzing data related to songs, including YouTube views, Anghami plays, and Spotify streams. It utilizes various APIs and web scraping techniques to extract relevant information and store it in a structured format.

Project Components:
youtubeviews.xlsx:

This Excel file contains data related to songs, including the song name, artist name, YouTube link, Anghami link, and Spotify link.
songs.xlsx:

Another Excel file used for storing the analytics data, including Spotify streams.
get_spotify_track_link:

A function that retrieves the Spotify link for a given song and artist using the Spotify API.
get_spotify_views:

A function that extracts the number of Spotify streams for a given song using web scraping techniques.
get_youtube_views:

A function that retrieves the number of YouTube views for a given video link using the youtubesearchpython library.
get_anghami_views:

A function that extracts the number of Anghami plays for a given song using web scraping techniques.
__main__ Block:

Reads the data from youtubeviews.xlsx and songs.xlsx.
Iterates through the data, fetching YouTube views, Anghami plays, and Spotify streams for each song.
Updates the songs.xlsx file with the collected Spotify streams data.
How to Use:
Dependencies Installation:

Install the required Python libraries using the following:
bash
Copy code
pip install youtubesearchpython urllib pandas spotipy requests beautifulsoup4
Spotify API Credentials:

You need to have Spotify API credentials to run the script successfully. Replace the placeholders in the get_spotify_track_link function with your actual credentials.
Execution:

Run the script:
bash
Copy code
python script_name.py
Ensure that both youtubeviews.xlsx and songs.xlsx are in the specified paths.
Notes:
Web Scraping:

Web scraping is used to extract data from Spotify and Anghami. Ensure that you are compliant with the terms of service of these platforms.
Spotify API:

The Spotify API is used to fetch Spotify track links. Make sure to replace the placeholder credentials with your own.
Excel Files:

The script reads data from youtubeviews.xlsx and updates songs.xlsx with Spotify streams information.
Additional Considerations:
Error Handling:

The script includes error-handling mechanisms for network-related issues and unsuccessful requests.
Data Availability:

Ensure that the YouTube, Anghami, and Spotify links provided in the input data are accessible and valid.
Author:
Minhal Awais
