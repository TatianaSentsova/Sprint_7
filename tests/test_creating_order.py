import pytest
import allure
from data import FakeBody, Data
from ApiShop import ApiRequests


class TestCreatingOrder:
    @allure.title('Успешное создание заказа без выбора/с выбором цвета самоката')
    @pytest.mark.parametrize('color', Data.COLOR)
    def test_create_order_diff_color(self, color):
        FakeBody.CREATE_ORDER['color'] = color
        response = ApiRequests.create_order(FakeBody.CREATE_ORDER)
        assert response.status_code == 201 and isinstance(ApiRequests.get_track_order(response), int)
        ApiRequests.cancel_order(response)
