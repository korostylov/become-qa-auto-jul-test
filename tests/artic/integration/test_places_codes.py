from applications.artic.api.http_status_codes import HttpStatusCodes

class TestArticApiPlaces:
    
     def test_get_fake_place(self, artic_api_client, fake_place):

        resp_code = artic_api_client.get_place_response_code(fake_place.id)

        # check that fake place is not found (404 is returned)
        assert resp_code == HttpStatusCodes.CODE_404
