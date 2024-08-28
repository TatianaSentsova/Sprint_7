from fake_data import FakeData


class Url:
    SCOOTER_URL = 'http://qa-scooter.praktikum-services.ru'
    ENDPOINT_COURIER = '/api/v1/courier'
    ENDPOINT_LOGIN = '/api/v1/courier/login'


class ResponseMessage:
    SUCCESS_CREATE = {"ok": True}
    THIS_LOGIN_ALREADY_USE = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    NOT_ENOUGH_DATA_FOR_CREATE = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    NOT_ENOUGH_DATA_FOR_LOGIN = {'code': 400, 'message': 'Недостаточно данных для входа'}
    ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}


class FakeBody:
    CREATE_COURIER_WITHOUT_REQUIRED_FIELD = [{"login": FakeData.login(), "password": '', "firstName": FakeData.first_name()},
                                             {"login": '', "password": FakeData.password(), "firstName": FakeData.first_name()}]
    LOGIN_COURIER = {"login": FakeData.login(), "password": FakeData.password()}