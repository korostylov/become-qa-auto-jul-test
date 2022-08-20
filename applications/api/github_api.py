import requests

class GitHubAPI:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
    
    def get_user(self, username):
        resp = requests.get(f"{self.base_url}/users/{username}")
        
        resp.raise_for_status()
        #if resp.raise_for_status != 200
        #    raise requests.HTTPError

        return resp.json()

    def get_repos(self, repos_search_param):
        resp = requests.get(
            #f"{self.base_url}/search/repositories?q={repos_search_param}",
            f"{self.base_url}/search/repositories",
            params={"q": repos_search_param}
            )
        
        resp.raise_for_status()

        return resp.json()

    