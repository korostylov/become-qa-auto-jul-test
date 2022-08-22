from config.config import Config
from providers.data.artworks_provider import ArtworksProvider
from providers.data.artworks import Artwork
from providers.data.base_data import BaseData

class TestArticApiArtworks:
    
    def test_get_existing_artwork(self, artic_api_client):
        artwork_existing = ArtworksProvider.existing_artwork()

        resp = artic_api_client.get_generic(f"{Config.ENDPOINT_ARTWORKS}/{artwork_existing.id}")
        

        artwork_from_get = Artwork(
            id = resp[BaseData.section_data][BaseData.field_id],
            api_model = resp[BaseData.section_data][BaseData.field_api_model],
            api_link = resp[BaseData.section_data][BaseData.field_api_link],
            title = resp[BaseData.section_data][BaseData.field_title],
            artist_display = resp[BaseData.section_data][BaseData.field_artist_display],
            place_of_origin = resp[BaseData.section_data][BaseData.field_place_of_origin]
        )

        # this comment is for checking if it really works
        #print(f"\nartwork_existing = {artwork_existing}")
        #print(f"\nartwork_from_get = {artwork_from_get}")

        # check that existing artwork is equal to the returned
        assert artwork_existing == artwork_from_get

    ###############################################################

    def test_get_fake_artwork(self, artic_api_client):
        artwork_fake = ArtworksProvider.fake_artwork()

        resp = artic_api_client.get_fake_entity(f"{Config.ENDPOINT_ARTWORKS}/{artwork_fake.id}")

        # check that fake artwork is not found (404 is returned)d
        assert resp.status_code == Config.STATUS_CODE_404

    ###############################################################
