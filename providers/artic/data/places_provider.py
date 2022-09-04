from faker import Faker

from models.artic.places import Place
from config.config import Config
from applications.artic.api.artic_endpoints import ArticEndpoints

class PlacesProvider:

    def generate_fake_place():

        faker = Faker()

        return Place(
            id = 1,
            api_model = faker.word(),
            api_link = faker.word(),
            title = faker.word(),
            type = faker.word(),
            tgn_id = faker.random_int(1, 100)
        )

    def existing_place():

        place_id = -5133

        return Place(
            id = place_id,
            api_model = "places",
            api_link = f"{Config.BASE_URL}{ArticEndpoints.PLACES}/{place_id}",
            title = "Cirebon",
            type = "No location",
            tgn_id = None
        )

    def remove_place(place):
        pass
