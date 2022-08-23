import os

from models.users import User

class UsersProvider:
    
    @staticmethod
    def fake_user():
        return User(
            login = 'somelogin123',
            password = 'fake_password'
        )
    
    @staticmethod
    def existing_user():
        return User(
            login = 'defunkt',
            password = 'password'
        )
    
    @staticmethod
    def existing_user_from_env():
        return {
            'login': os.environ.get("EXISTING_GITHUB_USER_LOGIN"),
            'id': os.environ.get("EXISTING_GITHUB_USER_ID")
        }
