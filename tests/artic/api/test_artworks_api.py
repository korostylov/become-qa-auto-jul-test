class TestArticApiArtworks:
    
    def test_get_existing_artwork(self, artic_api_client, existing_artwork):

        #get artwork
        artwork_from_get = artic_api_client.get_artwork(existing_artwork.id)

        # check that existing artwork is equal to the returned
        assert existing_artwork == artwork_from_get
