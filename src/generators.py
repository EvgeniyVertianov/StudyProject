from typing import Any


def filter_by_currency(transactions: list, currency: str) -> Any:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)."""
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item
