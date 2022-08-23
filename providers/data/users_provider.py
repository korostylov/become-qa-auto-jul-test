import os

from models.users import User

class UsersProvider:
    
    def fake_user():
        return User(
            login = 'somelogin123',
            password = 'fake_password'
        )
    
    def existing_user():
        return User(
            login = 'defunkt',
            password = 'password'
        )
