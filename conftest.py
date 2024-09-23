import pytest
from fake_data import FakeData
from api_shop import ApiRequests, ApiBodyBuilder


@pytest.fixture
def requests_courier_body():
    login = FakeData.login()
    password = FakeData.password()
    first_name = FakeData.first_name()
    courier_body = ApiBodyBuilder.build_courier_body(login, password, first_name)
    login_pass_body = ApiBodyBuilder.build_login_pass_body(login, password)
    yield [courier_body, login_pass_body]
    response = ApiRequests.login_courier(login_pass_body)
    id_courier = ApiRequests.get_id_courier(response)
    ApiRequests.delete_courier(id_courier)


@pytest.fixture
def courier_login_pass():
    login = FakeData.login()
    password = FakeData.password()
    first_name = FakeData.first_name()
    courier_body = ApiBodyBuilder.build_courier_body(login, password, first_name)
    ApiRequests.create_courier(courier_body)
    login_pass_body = ApiBodyBuilder.build_login_pass_body(login, password)
    yield login_pass_body.copy()
    response = ApiRequests.login_courier(login_pass_body)
    id_courier = ApiRequests.get_id_courier(response)
    ApiRequests.delete_courier(id_courier)
