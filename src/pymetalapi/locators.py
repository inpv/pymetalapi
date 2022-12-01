import re
from dataclasses import dataclass


@dataclass
class Locators:
    url_search_songs = 'search/ajax-advanced/searching/songs?'
    url_search_bands = 'search/ajax-advanced/searching/bands?'
    url_lyrics = 'release/ajax-view-lyrics/id/'
    lyrics_not_available = '(lyrics not available)'

    lyric_id_re = re.compile(r'id=.+[a-z]+.(?P<id>\d+)')
    band_name_re = re.compile(r'title="(?P<name>.*)\"')
    tags_re = re.compile(r'<[^>]+>')

    genres = ["black", "death", "doom", "stoner", "sludge", "electronic",
              "industrial", "experimental", "avant-garde", "folk", "viking",
              "pagan", "gothic", "grindcore", "groove", "heavy", "metalcore",
              "deathcore", "power", "progressive", "speed", "symphonic",
              "thrash"]