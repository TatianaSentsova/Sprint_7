from faker import Faker


class FakeData:
    @staticmethod
    def login():
        fake = Faker()
        login = fake.user_name()
        return login

    @staticmethod
    def password():
        fake = Faker()
        password = fake.password(length=10)
        return password

    @staticmethod
    def first_name():
        fake = Faker()
        first_name = fake.first_name()
        return first_name
