from applications.ui.base_ui import BaseUI
from applications.ui.locators.github_login_page_locators import GitHubLoginPageLocators as LoginPageLocators
from applications.ui.locators.github_home_page_locators import GitHubHomePageLocators as HomePageLocators
from models.users import User

class GitHubUI(BaseUI):
    
    def __init__(self, base_url, driver) -> None:
        self.base_url = base_url
        self.driver = driver

    def login (self, user: User):

        self.open(self.base_url)
        self.click(HomePageLocators.SIGNIN_MENU)

        self.wait_for_element_is_visible(LoginPageLocators.USERNAME).send_keys(user.login)
        self.wait_for_element_is_visible(LoginPageLocators.PASSWORD).send_keys(user.password)
        self.click(LoginPageLocators.SIGNIN_BUTTON)

        return True

    def get_validation_error(self):
        return self.wait_for_element_is_visible(LoginPageLocators.VALIDATION_MESSAGE).text
