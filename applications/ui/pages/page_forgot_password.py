class PageForgotPassword:

    def __init__(self, driver, base_url) -> None:
        self.driver = driver
        self.url = f"{base_url}/password_reset"

    def is_valid(self):
        return self.driver.title == "Forgot your password? · GitHub"