import requests
from data import Url, ResponseMessage, FakeBody


class TestLoginCourier:
    def test_login_courier(self, courier_login_pass):
        payload = courier_login_pass
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_LOGIN}', data=payload)
        assert response.status_code == 200 and isinstance(response.json()['id'], int)

    def test_login_without_login(self, courier_login_pass):
        payload = {"login": '', "password": courier_login_pass["password"]}
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_LOGIN}', data=payload)
        assert response.status_code == 400 and response.json() == ResponseMessage.NOT_ENOUGH_DATA_FOR_LOGIN

    def test_login_without_password(self, courier_login_pass):
        payload = {"login": courier_login_pass["login"], "password": ''}
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_LOGIN}', data=payload)
        assert response.status_code == 400 and response.json() == ResponseMessage.NOT_ENOUGH_DATA_FOR_LOGIN

    def test_login_without_error_login(self, courier_login_pass):
        payload = {"login": f'{courier_login_pass["login"]}f', "password": courier_login_pass["password"]}
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_LOGIN}', data=payload)
        assert response.status_code == 404 and response.json() == ResponseMessage.ACCOUNT_NOT_FOUND

    def test_login_without_error_password(self, courier_login_pass):
        payload = {"login": courier_login_pass["login"], "password": f'{courier_login_pass["password"]}f'}
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_LOGIN}', data=payload)
        assert response.status_code == 404 and response.json() == ResponseMessage.ACCOUNT_NOT_FOUND

    def test_login_non_existent_courier(self):
        payload = FakeBody.LOGIN_COURIER
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_LOGIN}', data=payload)
        assert response.status_code == 404 and response.json() == ResponseMessage.ACCOUNT_NOT_FOUND
