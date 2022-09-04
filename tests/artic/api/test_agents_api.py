class TestArticApiAgents:
    
    def test_get_existing_agent(self, artic_api_client, existing_agent):

        # get agent
        agent_from_get = artic_api_client.get_agent(existing_agent.id)

        # check that existing agent is equal to the returned
        assert existing_agent == agent_from_get
