from providers.data.places import Place
from config.config import Config

class PlacesProvider:

    def fake_place():
        return Place(
            id = 1,
            api_model = "model",
            api_link = "link",
            title = "title",
            type = "type",
            tgn_id = 1
        )

    def existing_place():
        return Place(
            id = -5133,
            api_model = "places",
            api_link = f"{Config.BASE_URL}{Config.ENDPOINT_PLACES}/-5133",
            title = "Cirebon",
            type = "No location",
            tgn_id = None
        )
