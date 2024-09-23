import requests
from data import Url


class ApiBodyBuilder:
    @staticmethod
    def build_courier_body(login, password, first_name):
        courier_body = {"login": login,
                        "password": password,
                        "firstName": first_name}
        return courier_body

    @staticmethod
    def build_login_pass_body(login, password):
        login_pass_body = {"login": login,
                           "password": password}
        return login_pass_body


class ApiRequests:
    @staticmethod
    def create_courier(body_courier):
        return requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}', json=body_courier)

    @staticmethod
    def login_courier(login_pass):
        return requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_LOGIN}', data=login_pass)

    @staticmethod
    def get_id_courier(response_login_courier):
        return response_login_courier.json()['id']

    @staticmethod
    def delete_courier(id_courier):
        return requests.delete(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}{id_courier}')

    @staticmethod
    def create_order(body_order):
        return requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_ORDER}', json=body_order)

    @staticmethod
    def cancel_order(response_order):
        return requests.put(f'{Url.SCOOTER_URL}{Url.ENDPOINT_CANCEL_ORDER}{ApiRequests.get_track_order(response_order)}')

    @staticmethod
    def get_track_order(response_order):
        return response_order.json()['track']

    @staticmethod
    def get_lists_order():
        return requests.get(f'{Url.SCOOTER_URL}{Url.ENDPOINT_ORDER}')
