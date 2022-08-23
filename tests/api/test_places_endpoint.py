from config.config import Config
from models.places import Place
from providers.data.places_provider import PlacesProvider
from providers.data.base_data import BaseData

class TestArticApiPlaces:
    
    def test_get_existing_place(self, artic_api_client):
        place_existing = PlacesProvider.existing_place()

        resp = artic_api_client.get_generic(f"{Config.ENDPOINT_PLACES}/{place_existing.id}")
        

        place_from_get = Place(
            id = resp[BaseData.section_data][BaseData.field_id],
            api_model = resp[BaseData.section_data][BaseData.field_api_model],
            api_link = resp[BaseData.section_data][BaseData.field_api_link],
            title = resp[BaseData.section_data][BaseData.field_title],
            type = resp[BaseData.section_data][BaseData.field_type],
            tgn_id = resp[BaseData.section_data][BaseData.field_tgn_id]
        )

        # this comment is for checking if it really works
        #print(f"\nplace_from_get_existing = {place_existing}")
        #print(f"\nplace_from_get = {place_from_get}")

        # check that existing place is equal to the returned
        assert place_existing == place_from_get

    ###############################################################

    def test_get_fake_place(self, artic_api_client):
        place_fake = PlacesProvider.fake_place()

        resp = artic_api_client.get_fake_entity(f"{Config.ENDPOINT_PLACES}/{place_fake.id}")

        # check that fake place is not found (404 is returned)
        assert resp.status_code == Config.STATUS_CODE_404

    ###############################################################
