import os


class Config:
    base_url = os.environ.get("BASE_URL_API", "https://api.github.com")
    base_url_ui = "https://github.com"