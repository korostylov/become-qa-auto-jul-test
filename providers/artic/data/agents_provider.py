from faker import Faker

from models.artic.agents import Agent
from config.config import Config
from applications.artic.api.artic_endpoints import ArticEndpoints

class AgentsProvider:

    def generate_fake_agent():

        faker = Faker()

        return Agent(
            id = 1,
            api_model = faker.word(),
            api_link = faker.word(),
            title = faker.word(),
            agent_type_title = faker.word(),
            agent_type_id = faker.random_int(1, 100)
        )

    def existing_agent():

        agent_id = 2

        return Agent(
            id = agent_id,
            api_model = "agents",
            api_link = f"{Config.BASE_URL}{ArticEndpoints.AGENTS}/{agent_id}",
            title = "Antiquarian Society",
            agent_type_title = "Museum Dept/Society",
            agent_type_id = 4
        )

    def remove_agent(agent):
        pass
