import pytest

from src.generators import filter_by_currency


# тест функции filter_by_currency
def test_filter_by_currency(transactions_for_test, currency="RUB"):
    filtered = filter_by_currency(transactions_for_test, currency="RUB")
    assert next(filtered) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(filtered) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


# тест функции filter_by_currency на другие валюты в ключе "code"
def test_filter_by_currency_incorrect_currency(transactions_for_test):
    filtered = filter_by_currency(transactions_for_test, "EUR")
    with pytest.raises(StopIteration):
        next(filtered)


# тест функции filter_by_currency на незаполненную валюту в ключе "code"
def test_filter_by_currency_none_currency(transactions_for_test):
    filtered = filter_by_currency(transactions_for_test, "")
    with pytest.raises(StopIteration):
        next(filtered)


# тест функции filter_by_currency на пустой список
def test_filter_by_currency_empty_list(transactions_empty_list):
    filtered = filter_by_currency(transactions_empty_list, "RUB")
    with pytest.raises(StopIteration):
        next(filtered)
