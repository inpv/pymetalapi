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

    band_dict = {
        "name": ['text', 'h1.band_name > a:nth-child(1)'],
        "url": ['href', 'h1.band_name > a:nth-child(1)'],
        "genre": ['text', 'dl.float_right > dd:nth-child(2)'],
        "themes": ['text', 'dl.float_right > dd:nth-child(4)'],
        "label": ['text', 'dl.float_right > dd:nth-child(6) > a:nth-child(1)'],
        "country": ['text', 'dl.float_left > dd:nth-child(2) > a:nth-child(1)'],
        "location": ['text', 'dl.float_left > dd:nth-child(4)'],
        "status": ['text', 'dl.float_left > dd:nth-child(6)'],
        "formed": ['text', 'dl.float_left > dd:nth-child(8)'],
        "years": ['text', 'dl.clear > dd:nth-child(2)'],
        "band_comment": ['text', '.band_comment']
    }
