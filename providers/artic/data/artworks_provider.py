from faker import Faker

from models.artic.artworks import Artwork
from config.config import Config
from applications.artic.api.artic_endpoints import ArticEndpoints

class ArtworksProvider:

    #def __init__(self) -> None:
    #    self.faker_test = Faker()

    #@staticmethod
    def generate_fake_artwork():

        faker = Faker()

        return Artwork(
            id = 1,
            api_model = faker.word(),
            api_link = faker.word(),
            title = faker.word(),
            artist_display = faker.word(),
            place_of_origin = faker.word()
        )

    def existing_artwork():

        artwork_id = 4

        return Artwork(
            id = artwork_id,
            api_model = "artworks",
            api_link = f"{Config.BASE_URL}{ArticEndpoints.ARTWORKS}/{artwork_id}",
            title = "Priest and Boy",
            artist_display = "Lawrence Carmichael Earle\nAmerican, 1845-1921",
            place_of_origin = "United States"
        )

    def remove_artwork(artwork):
        pass
