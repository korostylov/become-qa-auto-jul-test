from config.config import Config
from models.agents import Agent
from providers.data.agents_provider import AgentsProvider
from providers.data.base_data import BaseData

class TestArticApiAgents:
    
    def test_get_existing_agent(self, artic_api_client):
        agent_existing = AgentsProvider.existing_agent()

        resp = artic_api_client.get_generic(f"{Config.ENDPOINT_AGENTS}/{agent_existing.id}")
        

        agent_from_get = Agent(
            id = resp[BaseData.section_data][BaseData.field_id],
            api_model = resp[BaseData.section_data][BaseData.field_api_model],
            api_link = resp[BaseData.section_data][BaseData.field_api_link],
            title = resp[BaseData.section_data][BaseData.field_title],
            agent_type_title = resp[BaseData.section_data][BaseData.field_agent_type_title],
            agent_type_id = resp[BaseData.section_data][BaseData.field_agent_type_id]
        )

        # this comment is for checking if it really works
        #print(f"\nagent_from_get_existing = {agent_existing}")
        #print(f"\nagent_from_get = {agent_from_get}")

        # check that existing agent is equal to the returned
        assert agent_existing == agent_from_get

    ###############################################################

    def test_get_fake_agent(self, artic_api_client):
        agent_fake = AgentsProvider.fake_agent()

        resp = artic_api_client.get_fake_entity(f"{Config.ENDPOINT_AGENTS}/{agent_fake.id}")

        # check that fake agent is not found (404 is returned)
        assert resp.status_code == Config.STATUS_CODE_404

    ###############################################################
