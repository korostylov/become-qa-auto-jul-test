import pytest
import requests
from config.config import Config
from providers.data.users_provider import UsersProvider

def test_http_status_code200():
    resp = requests.get(Config.base_url)
    
    assert resp.status_code == 200
    #assert resp.text != "Design for failure."

def test_user_exists(github_api_client):
    
    user = UsersProvider.existing_user()
    api_user =  github_api_client.get_user(user['login'])
    
    assert api_user['login'] == user['login']
    assert api_user['id'] == user['id']

def test_user_non_exists(github_api_client):
    #resp = requests.get('https://api.github.com/users/defunkt2213123')
    #print(resp.__dict__)

    user = UsersProvider.fake_user()
    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user(user['login'])
    #assert user.status_code == 404
    #assert user['message'] == 'Not Found'