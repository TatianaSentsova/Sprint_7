import allure
import pytest
from ApiShop import ApiRequests, ApiBodyBuilder
from data import ResponseMessage
from fake_data import FakeData


class TestLoginCourier:
    @allure.title("Успешная авторизация зарегистрированного курьера при заполнении всех обязательных полей")
    def test_login_courier(self, courier_login_pass):
        response = ApiRequests.login_courier(courier_login_pass)
        assert response.status_code == 200 and isinstance(ApiRequests.get_id_courier(response), int)

    @allure.title("Нельзя авторизоваться зарегистрированному курьеру без заполнения обязательных полей")
    @pytest.mark.parametrize('empty_field', ('login', 'password'))
    def test_login_without_login(self, courier_login_pass, empty_field):
        courier_login_pass[empty_field] = ''
        response = ApiRequests.login_courier(courier_login_pass)
        assert response.status_code == 400 and response.json() == ResponseMessage.NOT_ENOUGH_DATA_FOR_LOGIN

    @allure.title("Нельзя авторизоваться зарегистрированному курьеру c не правильно заполненным обязательным полем")
    @pytest.mark.parametrize('error_in_data_field', ('login', 'password'))
    def test_login_without_error_login(self, courier_login_pass, error_in_data_field):
        error_data = f'{courier_login_pass[error_in_data_field]}f'
        courier_login_pass[error_in_data_field] = error_data
        response = ApiRequests.login_courier(courier_login_pass)
        assert response.status_code == 404 and response.json() == ResponseMessage.ACCOUNT_NOT_FOUND

    @allure.title("Нельзя авторизоваться под несуществующим пользователем")
    def test_login_non_existent_courier(self):
        login_pass_body = ApiBodyBuilder.build_login_pass_body(FakeData.login(), FakeData.password())
        response = ApiRequests.login_courier(login_pass_body)
        assert response.status_code == 404 and response.json() == ResponseMessage.ACCOUNT_NOT_FOUND
