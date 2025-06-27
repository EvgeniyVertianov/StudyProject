from typing import Any


def filter_by_currency(transactions: list, currency: str = "RUB") -> Any:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)."""
    for item in transactions:
        code = item.get("operationAmount", {}).get("currency", {}).get("code")
        if code == currency:
            yield item


def transaction_descriptions(transactions: list) -> Any:
    """Функция-генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for item in transactions:
        item = item.get("description")
        if item == "":
            yield "Описание операции не заполнено"
        else:
            yield item


def card_number_generator(start: int, stop: int) -> Any:
    """Функция-генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    start_card_number = "0000000000000000"
    nums = (num for num in range(start, stop + 1))
    for num in nums:
        card_number = start_card_number[: -len(str(num))] + str(num)
        if start > 16 or stop > 16:
            raise ValueError("В номере карты не может быть больше 16 цифр")
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
