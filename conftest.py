import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from applications.ui.github_ui import GitHubUI
from config.config import Config
from providers.data.users_provider import UsersProvider

#@pytest.fixture(scope = 'function/class/module/session')
@pytest.fixture()
def github_ui_client():

    driver = webdriver.Chrome(
        service = Service(ChromeDriverManager().install())
        )
    driver.maximize_window()

    github_ui_client = GitHubUI(Config.BASE_URL_UI, driver)

    yield github_ui_client

    github_ui_client.close_browser()
    print("----- End of tests.")

@pytest.fixture()
def fake_user():
    return UsersProvider.fake_user()
