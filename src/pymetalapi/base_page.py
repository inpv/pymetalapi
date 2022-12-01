import requests_cache
from pymetalapi.config import Config
from pymetalapi.util import get_random_user_agent
from requests_cache import remove_expired_responses


class BasePage:

    def __init__(self, url):
        requests_cache.install_cache(cache_name=Config.CACHE_FILE, expire_after=300)
        remove_expired_responses()

        self.session = requests_cache.CachedSession(cache_name=Config.CACHE_FILE)
        self.session.headers = {
            'User-Agent': get_random_user_agent(),
        }

        self.content = self._fetch_page_content(url)

    def _fetch_page_content(self, url) -> str:
        res = self.session.get(url)
        return res.text
