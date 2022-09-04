from applications.artic.api.artic_http_status_codes import ArticHttpStatusCodes

class TestArticApiAgents:
    
    def test_get_fake_agent(self, artic_api_client, fake_agent):

        resp_code = artic_api_client.get_not_existing_agent(fake_agent.id)

        # check that fake agent is not found (404 is returned)
        assert resp_code == ArticHttpStatusCodes.CODE_404
