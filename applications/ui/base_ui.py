from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseUI:

    def __init__(self, driver) -> None:
        self.driver = driver

    def wait_for_element_is_visible(
        self,
        locator,
        timeout = 5,
        poll_frequency = 0.1
        ):

        return WebDriverWait(self.driver, timeout, poll_frequency)\
            .until(EC.visibility_of_element_located(locator))

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait_for_element_is_visible(locator).click()

    def close_browser(self):
        self.driver.close()

    def get_title(self):
        return self.driver.title
