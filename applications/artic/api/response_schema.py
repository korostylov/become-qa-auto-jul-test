class ResponseSchema:

    # fields in response

    # pagination section
    section_pagination = "pagination"
    field_total = "total"
    field_limit = "limit"
    field_total_pages = "total_pages"
    field_current_page = "current_page"

    # data section
    section_data = "data"
    field_id = "id"
    field_api_model = "api_model"
    field_api_link = "api_link"
    field_title = "title"
    field_artist_display = "artist_display"
    field_place_of_origin = "place_of_origin"
    field_agent_type_title = "agent_type_title"
    field_agent_type_id = "agent_type_id"
    field_type = "type"
    field_tgn_id = "tgn_id"
    

    # info section
    section_info = "info"

    # config section
    section_config = "config"
    field_website_url = "website_url"

    # values in response
    value_website_url_artworks = "http://www.artic.edu"
    value_website_url_agents = value_website_url_artworks
    value_website_url_places = value_website_url_artworks
