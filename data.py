headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Аа",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}
product_ids = {
    "ids": [1, 2, 3]
}
def get_user_body(first_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = first_name
    # возвращается новый словарь с нужным значением firstName
    return current_body
