from pymetalapi.locators import Locators
from pymetalapi.util import get_element


class Bands:
    @staticmethod
    def get_band_data(tree):
        result = {}
        for key, values in Locators.band_dict.items():
            result[key] = get_element(tree=tree, sel_type=values[0], sel=values[1])

        return result
