class TestArticApiPlaces:
    
    def test_get_existing_place(self, artic_api_client, existing_place):

        # get place
        place_from_get = artic_api_client.get_place(existing_place.id)
        
        # check that existing place is equal to the returned
        assert existing_place == place_from_get
