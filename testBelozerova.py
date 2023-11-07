# Елизавета Белозерова, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import request, data

def get_track():
    responce = request.post_new_order(data.body)
    return responce.json()["track"]

def get_order():
    responce = request.get_order_track(str(get_track()))
    return responce

def test_status_code():
    responce = get_order()
    assert responce.status_code == 200


