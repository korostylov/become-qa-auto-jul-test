from selenium.webdriver.common.by import By
from random import randint

class GitHubLoginPageLocators:

    USERNAME = (By.ID, 'login_field')
    PASSWORD = (By.ID, 'password')
    SIGNIN_BUTTON = (By.XPATH, "//input[@type='submit']")

    VALIDATION_MESSAGE = (By.ID, 'js-flash-container')
