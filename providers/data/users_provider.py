from faker import Faker
from models.users import User

class UsersProvider:

    def generate_fake_user():
        faker = Faker()
        return User(
            login = faker.word(),
            password = faker.word()
        )

    def existing_user():
        return User(
            login = 'defunkt',
            password = 'password'
        )
