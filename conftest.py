import pytest

from applications.ui.github_ui import GitHubUI
from config.config import Config

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#@pytest.fixture(scope = 'function/class/module/session')
@pytest.fixture()
def github_ui_client():
    driver = webdriver.Chrome(
        service=Service(r"D:\Projects\Git\become-qa-auto-jul-test\chromedriver.exe")
        )

    github_ui_client = GitHubUI(Config.BASE_URL_UI, driver)
    
    yield github_ui_client
    
    github_ui_client.close_browser()
    print("----- End of tests.")
