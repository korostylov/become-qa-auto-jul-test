from selenium.webdriver.common.by import By

from applications.ui.pages.page_forgot_password import PageForgotPassword

class PageLogin:

    def __init__(self, driver, base_url) -> None:
        self.driver = driver
        self.base_url = base_url
        self.login_url = f"{self.base_url}/login"

    def navigate(self):
        self.driver.get(self.login_url)

    # 
    @property
    def login_field(self):
        # step 1: wait and find
        # step 2: validate field
        return self.driver.find_element(By.ID, "login_field")

    @property
    def password_field(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def login_btn(self):
        return self.driver.find_element(By.NAME, "commit")
    
    @property
    def sign_up_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Create an Account")
    
    
    @property
    def forgot_password_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Forgot password?")

    # Business Methods
    def login(self, username, password):

        self.navigate()
        self.login_field.send_keys(username)
        self.password_field.send_keys(password)

        self.login_btn.click()

        if self.is_login_error():
            return True

    def proceed_to_forgot_password_page(self):
        self.forgot_password_link.click()
        print("self.forgot_password_link.click() successful")
        return PageForgotPassword(self.driver, self.base_url)

    def proceed_to_sign_up(self):
        self.sign_up_link.click()

    # Validation Check
    def is_login_error(self):
        return self.driver.title != "Sign in to GitHub · GitHub"