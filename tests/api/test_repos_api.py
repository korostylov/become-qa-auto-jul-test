from providers.data.repositories_provider import RepositoriesProvider

def test_check_repos_can_be_found(github_api_client):
    repo_api = RepositoriesProvider.existing_repository()
    repos = github_api_client.get_repos(repo_api['name'])

    assert repos["total_count"] >= repo_api['total_count']
    assert len(repos["items"]) >= repo_api['items_count']

def test_check_repos_cannot_be_found(github_api_client):
    repo_api = RepositoriesProvider.non_existing_repository()
    repos = github_api_client.get_repos(repo_api['name'])

    assert repos["total_count"] == repo_api['total_count']
    assert len(repos["items"]) == repo_api['items_count']
    