import requests

class HTTPBase:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self.http_session = self.create_http_session()

    def create_http_session(self):
        return requests.Session()
    
    def get(
            self,
            endpoint,
            param_ids = "", # A comma-separated list of resource ids to retrieve
            param_limit = "", # The number of resources to return per page
            param_page = "", # The page of resources to retrieve
            param_fields = "", # A comma-separated list of fields to return per resource
            param_include = "", # A comma-separated list of subresource to embed in the returned resources
            ):
        
        return self.http_session.get(
            url = f"{self.base_url}{endpoint}",
            params = {
                "ids": param_ids,
                "limit": param_limit,
                "page": param_page,
                "fields": param_fields,
                "include": param_include,
                }
            ).json()
