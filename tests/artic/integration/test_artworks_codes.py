from applications.artic.api.artic_http_status_codes import ArticHttpStatusCodes

class TestArticApiArtworks:
    
    def test_get_fake_artwork(self, artic_api_client, fake_artwork):

        resp_code = artic_api_client.get_not_existing_artwork(fake_artwork.id)

        # check that fake artwork is not found (404 is returned)d
        assert resp_code == ArticHttpStatusCodes.CODE_404
