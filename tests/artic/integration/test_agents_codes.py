from applications.artic.api.http_status_codes import HttpStatusCodes

class TestArticApiAgents:
    
    def test_get_fake_agent(self, artic_api_client, fake_agent):

        resp_code = artic_api_client.get_agent_response_code(fake_agent.id)

        # check that fake agent is not found (404 is returned)
        assert resp_code == HttpStatusCodes.CODE_404
