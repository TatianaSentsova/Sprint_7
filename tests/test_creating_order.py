import requests
import pytest
from data import Url, FakeBody, Data


class TestCreatingOrder:
    @pytest.mark.parametrize('color', Data.COLOR)
    def test_create_order_diff_color(self, color):
        payload = FakeBody.CREATE_ORDER
        payload['color'] = color
        response = requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_ORDER}', json=payload)
        assert response.status_code == 201 and isinstance(response.json()['track'], int)
