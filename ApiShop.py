import json

import requests
from data import Url


class ApiRequests:
    @staticmethod
    def create_order(body_order):
        return requests.post(f'{Url.SCOOTER_URL}{Url.ENDPOINT_ORDER}', json=body_order)

    @staticmethod
    def cancel_order(response_order):
        return requests.put(f'{Url.SCOOTER_URL}{Url.ENDPOINT_CANCEL_ORDER}{ApiRequests.get_track_order(response_order)}')

    @staticmethod
    def get_track_order(response_order):
        return response_order.json()['track']
