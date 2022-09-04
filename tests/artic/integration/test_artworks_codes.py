from applications.artic.api.http_status_codes import HttpStatusCodes

class TestArticApiArtworks:
    
    def test_get_fake_artwork(self, artic_api_client, fake_artwork):

        resp_code = artic_api_client.get_artwork_response_code(fake_artwork.id)

        # check that fake artwork is not found (404 is returned)d
        assert resp_code == HttpStatusCodes.CODE_404
