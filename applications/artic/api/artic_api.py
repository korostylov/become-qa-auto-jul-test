from applications.artic.api.response_schema import ResponseSchema
from applications.artic.api.artic_endpoints import ArticEndpoints
from applications.artic.api.http_base import HTTPBase
from models.artic.artworks import Artwork
from models.artic.agents import Agent
from models.artic.places import Place

class ArticAPI(HTTPBase):

    def get_artwork(self, id):

        resp = self.get(
            endpoint = f"{ArticEndpoints.ARTWORKS}/{id}"
            )

        return Artwork(
            id = resp[ResponseSchema.section_data][ResponseSchema.field_id],
            api_model = resp[ResponseSchema.section_data][ResponseSchema.field_api_model],
            api_link = resp[ResponseSchema.section_data][ResponseSchema.field_api_link],
            title = resp[ResponseSchema.section_data][ResponseSchema.field_title],
            artist_display = resp[ResponseSchema.section_data][ResponseSchema.field_artist_display],
            place_of_origin = resp[ResponseSchema.section_data][ResponseSchema.field_place_of_origin]
        )

    def get_agent(self, id):

        resp = self.get(
            endpoint = f"{ArticEndpoints.AGENTS}/{id}"
            )

        return Agent(
            id = resp[ResponseSchema.section_data][ResponseSchema.field_id],
            api_model = resp[ResponseSchema.section_data][ResponseSchema.field_api_model],
            api_link = resp[ResponseSchema.section_data][ResponseSchema.field_api_link],
            title = resp[ResponseSchema.section_data][ResponseSchema.field_title],
            agent_type_title = resp[ResponseSchema.section_data][ResponseSchema.field_agent_type_title],
            agent_type_id = resp[ResponseSchema.section_data][ResponseSchema.field_agent_type_id]
        )

    def get_place(self, id):

        resp = self.get(
            endpoint = f"{ArticEndpoints.PLACES}/{id}"
            )

        return Place(
            id = resp[ResponseSchema.section_data][ResponseSchema.field_id],
            api_model = resp[ResponseSchema.section_data][ResponseSchema.field_api_model],
            api_link = resp[ResponseSchema.section_data][ResponseSchema.field_api_link],
            title = resp[ResponseSchema.section_data][ResponseSchema.field_title],
            type = resp[ResponseSchema.section_data][ResponseSchema.field_type],
            tgn_id = resp[ResponseSchema.section_data][ResponseSchema.field_tgn_id]
        )

    def get_not_existing_artwork(self, id):

        resp = self.get(
            endpoint = f"{ArticEndpoints.ARTWORKS}/{id}"
            )

        return  resp["status"]

    def get_not_existing_agent(self, id):

        resp = self.get(
            endpoint = f"{ArticEndpoints.AGENTS}/{id}"
            )

        return  resp["status"]

    def get_not_existing_place(self, id):

        resp = self.get(
            endpoint = f"{ArticEndpoints.PLACES}/{id}"
            )
        return resp["status"]
