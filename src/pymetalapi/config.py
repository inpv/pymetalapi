import os
import tempfile
from dataclasses import dataclass


@dataclass
class Config:
    CACHE_FILE = os.path.join(tempfile.gettempdir(), 'pymetalapi_cache')
    BASE_URL = 'https://www.metal-archives.com'
    RANDOM_BAND_URL = 'https://metal-archives.com/band/random'
