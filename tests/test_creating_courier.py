import requests
import pytest
from data import Url, ResponseMessage, FakeBody
from fake_data import FakeData


class TestCreatingCourier:
    def test_creating_new_courier(self, requests_courier_body):
        payload = requests_courier_body[0]
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}', data=payload)
        assert response.status_code == 201 and response.json() == ResponseMessage.SUCCESS_CREATE

    def test_creating_courier_with_required_fields(self, requests_courier_body):
        payload = requests_courier_body[1]
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}', data=payload)
        assert response.status_code == 201 and response.json() == ResponseMessage.SUCCESS_CREATE

    def test_creating_same_courier(self, login_pass):
        payload = login_pass
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}', data=payload)
        assert response.status_code == 409 and response.json() == ResponseMessage.THIS_LOGIN_ALREADY_USE

    def test_creating_same_login_courier(self, login_pass):
        payload = {'login': login_pass['login'], 'password': FakeData.password()}
        response_2 = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}', data=payload)
        assert response_2.status_code == 409 and response_2.json() == ResponseMessage.THIS_LOGIN_ALREADY_USE

    @pytest.mark.parametrize('registration_data', FakeBody.CREATE_COURIER_WITHOUT_REQUIRED_FIELD)
    def test_creating_courier_without_required_field(self, registration_data):
        payload = registration_data
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}', data=payload)
        assert response.status_code == 400 and response.json() == ResponseMessage.NOT_ENOUGH_DATA_FOR_CREATE
