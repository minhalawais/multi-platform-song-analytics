from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import time
# Login details
username = "kholoud.albanna@mdlbeast.com"
password = "0504322341Kk."
song_url = "https://insights.theorchard.com/catalog/songs"


def create_chrome_bot():
    o = webdriver.ChromeOptions()
    o.add_argument("disable-extensions")
    o.add_argument("--window-size=800,600")
    o.add_argument("user-data-dir=C:\\Users\minha\\AppData\\Local\Google\\Chrome\\User Data")
    o.add_argument("profile-directory=Profile 2") #enter profile here
    driver = webdriver.Chrome(executable_path=r"\chromedriver.exe",options=o)
    return driver
def get_orchard_song_links(driver):
    df1 = pd.read_excel("youtubeviews.xlsx")
    return df1["Song Name"].values.tolist(),df1["ISRC"].values.tolist()

def get_song_views(driver,songs_link):
    tab_index =0
    open_tab = 0
    index = 0
    spotipy_list = []
    apple_list = []
    for song in songs_link:
        apple_link = f"https://insights.theorchard.com/song/{song}/?areaView=disabled&store=1&source=store"
        spotify_link = f"https://insights.theorchard.com/song/{song}/?areaView=disabled&store=286&source=store"
        while open_tab < 9:
            driver.execute_script("window.open('');")
            open_tab =open_tab + 1
        driver.switch_to.window(driver.window_handles[tab_index])
        driver.get(apple_link)
        driver.switch_to.window(driver.window_handles[tab_index+1])
        driver.get(spotify_link)
        tab_index = tab_index + 2
        if tab_index == 10:
            while index < 10:

                driver.switch_to.window(driver.window_handles[index])
                time.sleep(1)
                main_page_html = driver.page_source
                soup = BeautifulSoup(main_page_html, 'html.parser')
                spans = soup.find_all('td', {'class': 'cell-streams col-sorted text-right'})
                songs_views = [span.get_text() for span in spans]
                if songs_views:
                    if index %2==0:
                        apple_list.append(songs_views[0])
                        print(songs_views[0])
                    elif index%2!=0:
                         spotipy_list.append(songs_views[0])
                         print(songs_views[0])
                else:
                    if index %2==0:
                        apple_list.append(None)
                    elif index%2!=0:
                         spotipy_list.append(None)
                index = index + 1
            tab_index = 0
            index = 0
    return apple_list,spotipy_list
driver = create_chrome_bot()
song_name,songs_link_list = get_orchard_song_links(driver)
apple_songs,spotify_songs = get_song_views(driver,songs_link_list)
df1 = pd.read_excel("songs.xlsx")
df1["Spotify streams"] = pd.Series(spotify_songs)
df1["Apple Music streams"] = pd.Series(apple_songs)
df1.to_excel("songs.xlsx",index=False)


