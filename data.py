from fake_data import FakeData


class Url:
    SCOOTER_URL = 'http://qa-scooter.praktikum-services.ru'
    ENDPOINT_COURIER = '/api/v1/courier'
    ENDPOINT_LOGIN = '/api/v1/courier/login'
    ENDPOINT_ORDER = '/api/v1/orders'
    ENDPOINT_CANCEL_ORDER = '/api/v1/orders/cancel?track='


class ResponseMessage:
    SUCCESS_CREATE = {"ok": True}
    THIS_LOGIN_ALREADY_USE = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    NOT_ENOUGH_DATA_FOR_CREATE = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    NOT_ENOUGH_DATA_FOR_LOGIN = {'code': 400, 'message': 'Недостаточно данных для входа'}
    ACCOUNT_NOT_FOUND = {'code': 404, 'message': 'Учетная запись не найдена'}
    FLAG_ORDERS_LIST = 'orders'


class FakeBody:
    LOGIN_COURIER = {"login": FakeData.login(), "password": FakeData.password()}
    CREATE_ORDER = {"firstName": FakeData.first_name(),
                    "lastName": FakeData.last_name(),
                    "address": FakeData.address(),
                    "metroStation": FakeData.metro_station(),
                    "phone": FakeData.phone(),
                    "rentTime": FakeData.rent_time(),
                    "deliveryDate": FakeData.delivery_date(),
                    "comment": FakeData.comment(),
                    "color": []}


class Data:
    COLOR = [['BLACK', 'GREY'], ['BLACK'], ['GREY'], ['']]
