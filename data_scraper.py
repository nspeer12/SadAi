# credit: https://www.johnwmillr.com/scraping-genius-lyrics/
import lyricsgenius as genius
from bs4 import BeautifulSoup
import re

api = genius.Genius('4qDdMEp4tR4IOTGTNWRWFdbw2vaB3baJ-3UGyefet7MupqKwz4tG9ZyoDwJYE_sw')
artist = api.search_artist('Lil Peep', max_songs = 1000)


artist.save_lyrics()
print(artist)
