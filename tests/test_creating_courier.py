import pytest
import allure
from data import ResponseMessage
from api_shop import ApiRequests, ApiBodyBuilder
from fake_data import FakeData


class TestCreatingCourier:
    @allure.title("Успешное создание курьера при заполнении всех полей.")
    def test_creating_new_courier(self, requests_courier_body):
        response = ApiRequests.create_courier(requests_courier_body[0])
        assert response.status_code == 201 and response.json() == ResponseMessage.SUCCESS_CREATE

    @allure.title("Успешное создание курьера при заполнении только обязательных полей")
    def test_creating_courier_with_required_fields(self, requests_courier_body):
        response = ApiRequests.create_courier(requests_courier_body[1])
        assert response.status_code == 201 and response.json() == ResponseMessage.SUCCESS_CREATE

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_creating_same_courier(self, courier_login_pass):
        response = ApiRequests.create_courier(courier_login_pass)
        assert response.status_code == 409 and response.json() == ResponseMessage.THIS_LOGIN_ALREADY_USE

    @allure.title("Нельзя создать двух курьеров c одинаковым логином")
    def test_creating_same_login_courier(self, courier_login_pass):
        courier_login_pass['password'] = FakeData.password()
        response = ApiRequests.create_courier(courier_login_pass)
        assert response.status_code == 409 and response.json() == ResponseMessage.THIS_LOGIN_ALREADY_USE

    @allure.title("Нельзя создать курьера, не заполнив одно из обязательных полей")
    @pytest.mark.parametrize(
        'registration_data',
        [
            ApiBodyBuilder.build_courier_body(FakeData.login(), '', FakeData.first_name()),
            ApiBodyBuilder.build_courier_body('', FakeData.password(), FakeData.first_name())
        ]
    )
    def test_creating_courier_without_required_field(self, registration_data):
        response = ApiRequests.create_courier(registration_data)
        assert response.status_code == 400 and response.json() == ResponseMessage.NOT_ENOUGH_DATA_FOR_CREATE
