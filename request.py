import requests


import configuration

import data

#создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)

# получение информации конкретном заказе
def get_order_track(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + track_id)

