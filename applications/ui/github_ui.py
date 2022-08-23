from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from applications.ui.locators.github_login_page_locators import GitHubLoginPageLocators as LoginPageLocators
from applications.ui.locators.github_home_page_locators import GitHubHomePageLocators as HomePageLocators

class GitHubUI:
    
    def __init__(self, base_url, driver) -> None:
        self.base_url = base_url
        self.driver = driver

    def element_is_visible(
            self,
            locator,
            timeout = 5,
            poll_frequency = 0.1):
        return Wait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.element_is_visible(locator).click()

    def login (self, username, user_password):

        self.open(self.base_url)
        self.click(HomePageLocators.SIGNIN_MENU)

        self.element_is_visible(LoginPageLocators.USERNAME).send_keys(username)
        self.element_is_visible(LoginPageLocators.PASSWORD).send_keys(user_password)
        self.click(LoginPageLocators.SIGNIN_BUTTON)

        return True

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title
    
    def get_validation_error(self):
        return self.element_is_visible(LoginPageLocators.VALIDATION_MESSAGE).text
