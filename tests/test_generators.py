import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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


# тест функции transaction_descriptions
def test_transaction_descriptions(transactions_for_test):
    filtered = transaction_descriptions(transactions_for_test)
    assert next(filtered) == "Перевод организации"
    assert next(filtered) == "Перевод со счета на счет"
    assert next(filtered) == "Перевод со счета на счет"
    assert next(filtered) == "Перевод с карты на карту"


# тест функции transaction_descriptions на незаполненное описание операции в ключе "description"
def test_transaction_descriptions_none_description(transactions_none_description):
    filtered = transaction_descriptions(transactions_none_description)
    assert next(filtered) == "Описание операции не заполнено"
    assert next(filtered) == "Описание операции не заполнено"


# тест функции transaction_descriptions на пустой список
def test_transaction_descriptions_empty_list(transactions_empty_list):
    filtered = transaction_descriptions(transactions_empty_list)
    with pytest.raises(StopIteration):
        next(filtered)


# тест функции card_number_generator
def test_card_number_generator():
    gen = card_number_generator(1, 3)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"


# тест функции card_number_generator на неверный формат номера карты
def test_incorrect_card_number_generator():
    gen = card_number_generator(10000000000000000, 100000000000000001)
    with pytest.raises(ValueError) as exc_info:
        next(gen)  # Вызываем генератор
    assert str(exc_info.value) == "В номере карты не может быть больше 16 цифр"
