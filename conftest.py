#from pytest import fixture
import pytest

from applications.api.github_api import GitHubAPI
from applications.ui.github_ui import GitHubUI
from config.config import Config

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#@pytest.fixture(scope = 'function/class/module/session')
@pytest.fixture(scope = 'session')
def github_api_client():
    github_api_client = GitHubAPI(Config.base_url)

    yield github_api_client
    print("End of test.")

@pytest.fixture()#(scope = 'session')
def github_ui_client():
    driver = webdriver.Chrome(
        service=Service(r"D:\Projects\Git\become-qa-auto-jul-test\chromedriver.exe")
        )

    github_ui_client = GitHubUI(Config.base_url_ui, driver)
    
    yield github_ui_client
    
    github_ui_client.close_browser()
    print("End of test.")


