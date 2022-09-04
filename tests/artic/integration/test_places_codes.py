from applications.artic.api.artic_endpoints import ArticEndpoints
from applications.artic.api.artic_http_status_codes import ArticHttpStatusCodes

class TestArticApiPlaces:
    
     def test_get_fake_place(self, artic_api_client, fake_place):

        resp_code = artic_api_client.get_not_existing_place(fake_place.id)

        # check that fake place is not found (404 is returned)
        assert resp_code == ArticHttpStatusCodes.CODE_404
