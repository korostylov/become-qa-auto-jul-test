import pytest

from applications.api.artic_api import ArticAPI
from config.config import Config

#@pytest.fixture(scope = 'function/class/module/session')
@pytest.fixture(scope = 'session')
def artic_api_client():
    artic_api_client = ArticAPI(Config.BASE_URL)

    yield artic_api_client
    print("End of test.")
