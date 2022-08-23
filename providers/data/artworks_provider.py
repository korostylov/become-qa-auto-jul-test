from models.artworks import Artwork
from config.config import Config

class ArtworksProvider:

    def fake_artwork():
        return Artwork(
            id = 1,
            api_model = "model",
            api_link = "link",
            title = "title",
            artist_display = "artist",
            place_of_origin = "place"
        )

    def existing_artwork():
        return Artwork(
            id = 4,
            api_model = "artworks",
            api_link = f"{Config.BASE_URL}{Config.ENDPOINT_ARTWORKS}/4",
            title = "Priest and Boy",
            artist_display = "Lawrence Carmichael Earle\nAmerican, 1845-1921",
            place_of_origin = "United States"
        )
