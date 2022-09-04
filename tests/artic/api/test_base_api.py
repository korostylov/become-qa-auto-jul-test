import pytest
from random import randint

from applications.artic.api.response_schema import ResponseSchema
from applications.artic.api.artic_endpoints import ArticEndpoints

class TestArticApiBase:

    # list of available endpoints
    endpoints = [
        ArticEndpoints.ARTWORKS,
        ArticEndpoints.AGENTS,
        ArticEndpoints.PLACES
    ]

    # max number of elements per page
    max_limit = 100

    @pytest.mark.parametrize('endpoint', endpoints)
    def test_base_check_endpoint_return_data(self, artic_api_client, endpoint):

        resp_total = artic_api_client.get_field_total(endpoint)

        # check that at least one element is returned in response
        assert resp_total > 0

    ###############################################################

    urls = [
        (ArticEndpoints.ARTWORKS, ResponseSchema.value_website_url_artworks),
        (ArticEndpoints.AGENTS, ResponseSchema.value_website_url_agents),
        (ArticEndpoints.PLACES, ResponseSchema.value_website_url_places)
    ]

    @pytest.mark.parametrize('endpoint, website_url', urls)
    def test_base_check_website_url(self, artic_api_client, endpoint, website_url):

        resp_url = artic_api_client.get_field_website_url(endpoint)

        # check that returned website_url is equal to the configured
        assert resp_url == website_url

    ###############################################################

    @pytest.mark.parametrize('endpoint', endpoints)
    def test_base_return_specific_number_of_entities(self, artic_api_client, endpoint):

        # get random page in range [1, total pages]
        random_limit = randint(1, self.max_limit)

        resp_data_length = artic_api_client.get_length_section_data_with_limit(endpoint, random_limit)

        # check that request with specific limit returns exact number of entities
        assert resp_data_length == random_limit

    ###############################################################

    @pytest.mark.parametrize('endpoint', endpoints)
    def test_base_return_specific_page(self, artic_api_client, endpoint):
        
        # get total pages
        resp_total_pages = artic_api_client.get_field_total_pages(endpoint)

        # get random page in range [1, total pages]
        random_page = randint(1, resp_total_pages)

        resp_current_page = artic_api_client.get_field_current_page(endpoint, random_page)
        
        # check that request with specific page returns exact page
        assert resp_current_page == random_page

    ###############################################################

    @pytest.mark.parametrize('endpoint', endpoints)
    def test_base_return_only_one_field(self, artic_api_client, endpoint):

        resp_data_section = artic_api_client.get_section_data_with_only_title_field(endpoint)

        resp_data_section_len = len(resp_data_section)

        # check that each element 'data' array contains only 1 item
        for i in range(0, resp_data_section_len):
            assert len(resp_data_section[i]) == 1
