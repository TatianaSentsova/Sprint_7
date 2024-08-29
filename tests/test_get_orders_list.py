import allure
from data import ResponseMessage
from ApiShop import ApiRequests


class TestGetOrdersList:
    @allure.title('Получение списка заказов')
    def test_get_list_order(self):
        response = ApiRequests.get_lists_order()
        assert response.status_code == 200
        assert ResponseMessage.FLAG_ORDERS_LIST in response.json()
