import requests
import pytest
from data import Url, FakeBody, Data
from ApiShop import ApiRequests


class TestCreatingOrder:
    @pytest.mark.parametrize('color', Data.COLOR)
    def test_create_order_diff_color(self, color):
        payload = FakeBody.CREATE_ORDER
        payload['color'] = color
        response = ApiRequests.create_order(payload)
        assert response.status_code == 201 and isinstance(ApiRequests.get_track_order(response), int)
        ApiRequests.cancel_order(response)
