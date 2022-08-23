from models.agents import Agent
from config.config import Config

class AgentsProvider:

    def fake_agent():
        return Agent(
            id = 1,
            api_model = "model",
            api_link = "link",
            title = "title",
            agent_type_title = "agent_type_title",
            agent_type_id = 1
        )

    def existing_agent():
        return Agent(
            id = 2,
            api_model = "agents",
            api_link = f"{Config.BASE_URL}{Config.ENDPOINT_AGENTS}/2",
            title = "Antiquarian Society",
            agent_type_title = "Museum Dept/Society",
            agent_type_id = 4
        )
