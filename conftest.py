import pytest

from config.config import Config
from applications.artic.api.artic_api import ArticAPI
from providers.artic.data.agents_provider import AgentsProvider
from providers.artic.data.artworks_provider import ArtworksProvider
from providers.artic.data.places_provider import PlacesProvider

#@pytest.fixture(scope = 'function/class/module/session')
@pytest.fixture(scope = 'session')
def artic_api_client():
    artic_api_client = ArticAPI(Config.BASE_URL)

    yield artic_api_client

@pytest.fixture(scope = 'function')
def existing_artwork():
    return ArtworksProvider.existing_artwork()

@pytest.fixture(scope = 'function')
def fake_artwork():
    
    # this is an example of '@staticmethod' usage.
    # if 'generate_fake_artwork()' has '@staticmethod',
    # it can be called as method or using object of that class.
    # also,  @staticmethod doesn't have 'self' in parameters
    # and cannot get or set object parameters via 'self'

    #artwork_provider = ArtworksProvider()
    #fake_artwork = artwork_provider.generate_fake_artwork()

    fake_artwork = ArtworksProvider.generate_fake_artwork()

    yield fake_artwork

    ArtworksProvider.remove_artwork(fake_artwork)

@pytest.fixture(scope = 'function')
def existing_agent():
    return AgentsProvider.existing_agent()

@pytest.fixture(scope = 'function')
def fake_agent():

    fake_agent = AgentsProvider.generate_fake_agent()

    yield fake_agent

    AgentsProvider.remove_agent(fake_agent)

@pytest.fixture(scope = 'function')
def existing_place():
    return PlacesProvider.existing_place()

@pytest.fixture(scope = 'function')
def fake_place():

    fake_place = PlacesProvider.generate_fake_place()

    yield fake_place

    PlacesProvider.remove_place(fake_place)
