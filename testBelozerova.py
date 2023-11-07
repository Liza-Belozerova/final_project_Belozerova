# Елизавета Белозерова, 10-я когорта — Финальный проект. Инженер по тестированию плюс
import request, data

# сохранение трек номера
def get_track():
    responce = request.post_new_order(data.body)
    return responce.json()["track"]

# подставили трек номер в запрос на получение информации о заказе
def get_order():
    responce = request.get_order_track(str(get_track()))
    return responce

# тест на проверку приходит ли в ответе 200 код
def test_status_code():
    responce = get_order()
    assert responce.status_code == 200


