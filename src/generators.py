from typing import Any


def filter_by_currency(transactions: list, currency: str) -> Any:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)."""
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


def transaction_descriptions(transactions: list) -> Any:
    """Функция-генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for item in transactions:
        item = item.get("description")
        if item == "":
            yield "Описание операции не заполнено"
        else:
            yield item


# if __name__ == "__main__":
#     transactions = [
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "asd",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702",
#             },
#             {
#                 "id": 142264268,
#                 "state": "EXECUTED",
#                 "date": "2019-04-04T23:20:05.206878",
#                 "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#                 "description": "",
#                 "from": "Счет 19708645243227258542",
#                 "to": "Счет 75651667383060284188",
#             },
#         ]
#
#     gen = transaction_descriptions(transactions)
#
#     print(next(gen))
#     print(next(gen))
