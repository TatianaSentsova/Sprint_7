import pytest
import requests
from data import Url
from fake_data import FakeData


@pytest.fixture
def requests_courier_body():
    login = FakeData.login()
    password = FakeData.password()
    first_name = FakeData.first_name()
    create_courier_body = {"login": login,
                           "password": password,
                           "firstName": first_name}
    login_pass_body = {"login": login,
                       "password": password}
    yield [create_courier_body, login_pass_body]
    response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_LOGIN}', data=login_pass_body)
    id_courier = response.json()["id"]
    requests.delete(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}{id_courier}')


@pytest.fixture
def login_pass():
    login = FakeData.login()
    password = FakeData.password()
    first_name = FakeData.first_name()
    create_courier_body = {"login": login,
                           "password": password,
                           "firstName": first_name}
    requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}', data=create_courier_body)
    login_pass_body = {"login": login,
                       "password": password}
    yield login_pass_body
    response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_LOGIN}', data=login_pass_body)
    id_courier = response.json()["id"]
    requests.delete(f'{Url.SCOOTER_URL}{Url.ENDPOINT_COURIER}{id_courier}')