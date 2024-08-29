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

    @staticmethod
    def last_name():
        fake = Faker()
        last_name = fake.last_name()
        return last_name

    @staticmethod
    def address():
        fake = Faker()
        address = fake.street_address()
        return address

    @staticmethod
    def phone():
        fake = Faker("ru_RU")
        phone = fake.phone_number()
        return phone

    @staticmethod
    def delivery_date():
        fake = Faker()
        delivery_date = fake.date_this_month(before_today=False, after_today=True)
        return delivery_date.strftime("%Y-%m-%d")

    @staticmethod
    def rent_time():
        fake = Faker()
        rent_time = fake.pyint(min_value=1, max_value=7)
        return rent_time

    @staticmethod
    def metro_station():
        fake = Faker()
        metro_station = fake.pyint(min_value=1, max_value=220)
        return metro_station

    @staticmethod
    def comment():
        fake = Faker()
        comment = fake.pystr(min_chars=5, max_chars=10)
        return comment
