import os

class UsersProvider:
    
    @staticmethod
    def fake_user():
        return {
            'login': 'somelogin123',
            'id': 12345,
            'password': 'fake_password'
        }
    
    @staticmethod
    def existing_user():
        return {
            'login': 'defunkt',
            'id': 2,
            'password': 'password'
        }
    
    @staticmethod
    def existing_user_from_env():
        return {
            'login': os.environ.get("EXISTING_GITHUB_USER_LOGIN"),
            'id': os.environ.get("EXISTING_GITHUB_USER_ID")
        }
