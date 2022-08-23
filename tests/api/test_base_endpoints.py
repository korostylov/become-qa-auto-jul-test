import pytest
from random import randint
from config.config import Config
from providers.data.base_data import BaseData

class TestArticApiBase:

    # list of available endpoints
    endpoints = [
        Config.ENDPOINT_ARTWORKS,
        Config.ENDPOINT_AGENTS,
        Config.ENDPOINT_PLACES
    ]

    # max number of elements per page
    max_limit = 100

    @pytest.mark.parametrize('endpoint', endpoints)
    def test_base_check_endpoint_return_data(self, artic_api_client, endpoint):
        resp = artic_api_client.get_generic(endpoint)

        # check that at least one element is returned in response
        assert resp[BaseData.section_pagination][BaseData.field_total] > 0

    ###############################################################

    urls = [
        (Config.ENDPOINT_ARTWORKS, BaseData.value_website_url_artworks),
        (Config.ENDPOINT_AGENTS, BaseData.value_website_url_agents),
        (Config.ENDPOINT_PLACES, BaseData.value_website_url_places)
    ]

    @pytest.mark.parametrize('endpoint, website_url', urls)
    def test_base_check_website_url(self, artic_api_client, endpoint, website_url):

        resp = artic_api_client.get_generic(endpoint)

        # check that returned website_url is equal to the configured
        assert resp[BaseData.section_config][BaseData.field_website_url] == website_url

    ###############################################################

    @pytest.mark.parametrize('endpoint', endpoints)
    def test_base_return_specific_number_of_entities(self, artic_api_client, endpoint):

        # get random page in range [1, total pages]
        random_limit = randint(1, self.max_limit)

        resp = artic_api_client.get_generic(
            endpoint,
            param_limit = random_limit
            )
        
        # check that request with specific limit returns exact number of entities
        assert len(resp[BaseData.section_data]) == random_limit

    ###############################################################

    @pytest.mark.parametrize('endpoint', endpoints)
    def test_base_return_specific_page(self, artic_api_client, endpoint):
        
        # get total pages
        resp = artic_api_client.get_generic(endpoint)
        resp_total_pages = resp[BaseData.section_pagination][BaseData.field_total_pages]
        
        # get random page in range [1, total pages]
        random_page = randint(1, resp_total_pages)

        resp = artic_api_client.get_generic(
            endpoint,
            param_page = random_page
            )
        
        # check that request with specific page returns exact page
        assert resp[BaseData.section_pagination][BaseData.field_current_page] == random_page

    ###############################################################

    @pytest.mark.parametrize('endpoint', endpoints)
    def test_base_return_only_one_field(self, artic_api_client, endpoint):
        resp = artic_api_client.get_generic(
            endpoint,
            param_fields = BaseData.field_title
            )
        #print(resp)
        print(len(resp[BaseData.section_data]))

        date_array_len = len(resp[BaseData.section_data])

        # check that only each element in one element 'data' array contains only 1 item
        for i in range(0, date_array_len):
            assert len(resp[BaseData.section_data][i]) == 1

    ###############################################################
