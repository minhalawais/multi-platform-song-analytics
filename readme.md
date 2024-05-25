# Songs Data Analysis

This project aims to analyze the views and streams of songs from multiple platforms, including YouTube, Spotify, and Anghami. The data is read from Excel files, and various web scraping and API techniques are used to gather the necessary information.

## Prerequisites

- Python 3.x
- `pandas` library
- `spotipy` library
- `requests` library
- `BeautifulSoup` library
- `youtubesearchpython` library
- `html5lib` library

## Installation

1. Clone the repository to your local machine.

2. Install the required Python libraries:
    ```sh
    pip install pandas spotipy requests beautifulsoup4 youtubesearchpython html5lib
    ```

3. Obtain Spotify API credentials:
    - Create a new app on the Spotify Developer Dashboard.
    - Note the `client_id` and `client_secret` from your app settings.

## Usage

1. Place your Excel files in the specified directory paths. The Excel files should have the following structure:
    - `youtubeviews.xlsx` should contain columns: `Song Name`, `Artist Name`, `Youtube link`, `Anghami Link`, `Spotify Link`
    - `songs.xlsx` should contain a column: `Spotify streams`

2. Modify the script with your Spotify API credentials:
    ```python
    client_id = 'your_spotify_client_id'
    client_secret = 'your_spotify_client_secret'
    ```

3. Run the script:
    ```sh
    python your_script_name.py
    ```

## Functions

### get_spotify_track_link(song_name, artist_name)
Searches for a track on Spotify using the song name and artist name, and returns the Spotify track link.

### get_spotify_views(song_link, song_name)
Fetches the number of views/streams for a given Spotify track link and song name.

### get_youtube_views(song_link)
Fetches the number of views for a given YouTube video link using `youtubesearchpython`.

### get_anghami_views(song_link)
Fetches the number of views for a given Anghami track link.

## Main Script

The main script reads data from the Excel files, processes each song to fetch the views and streams from various platforms, and updates the Excel files with the gathered information.

## Example Output

The script will output the number of songs found and not found with Spotify views in the Excel file. It will also print the updated DataFrame.

## Notes

- Ensure you have the necessary permissions to access the API and web scraping functionalities.
- Be aware of the rate limits for the APIs and handle retries appropriately.

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Spotify API](https://developer.spotify.com/documentation/web-api/)
- [YouTube Data API](https://developers.google.com/youtube/v3)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [youtubesearchpython Documentation](https://github.com/alexmercerind/youtube-search-python)
