from pymetalapi.endpoints.bands import Bands
from pymetalapi.base_page import BasePage
from pymetalapi.config import Config


class Search:
    # TODO: link these methods to FASTAPI queries, with Uvicorn simulating the server responses

    @staticmethod
    def search_random_band():
        return Bands.get_band_data(BasePage(url=Config.RANDOM_BAND_URL).content)
