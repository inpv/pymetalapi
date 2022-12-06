from pymetalapi.endpoints.bands import Bands
from pymetalapi.base_page import BasePage
from pymetalapi.config import Config


class Search:

    @staticmethod
    def search_random_band():
        return Bands.get_band_data(BasePage(url=Config.RANDOM_BAND_URL).content)
