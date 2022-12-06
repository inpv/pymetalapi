import requests_cache
from lxml import html
from datetime import timedelta
from pymetalapi.config import Config
from pymetalapi.util import get_random_user_agent
from requests_cache import remove_expired_responses


class BasePage:

    def __init__(self, url):
        requests_cache.install_cache(cache_name=Config.CACHE_FILE, expire_after=timedelta(hours=1))
        remove_expired_responses()

        self.session = requests_cache.CachedSession(backend='memory',
                                                    expire_after=timedelta(hours=1))
        self.session.headers = {
            'User-Agent': get_random_user_agent(),
        }

        self.content = self._fetch_page_content(url)

    def _fetch_page_content(self, url) -> str:
        response = self.session.get(url)  # getting the response
        tree = html.fromstring(response.content)  # loading it into the html parser
        return tree
