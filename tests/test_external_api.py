from typing import Any
from unittest.mock import patch

import pytest

from src.external_api import API_KEY, get_transaction_amount


# проверяем код на положительный исход при использовании рублей
@pytest.mark.parametrize(
    "transaction, expected",
    [
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            "31957.58",
        )
    ],
)
def test_get_transaction_amount_rub(
    transaction: dict[str, int | str | dict[str, str | dict[str, str]]], expected: str
) -> None:
    assert get_transaction_amount(transaction) == expected


# проверяем код на положительный исход при использовании иностранной валюты
@patch("requests.request")
def test_get_transaction_amount_usd(
    mock_get: Any, transaction_usd: dict[str, int | str | dict[str, str | dict[str, str]]]
) -> None:
    response = mock_get.return_value
    response.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1747374004, "rate": 80.000089},
        "date": "2025-05-16",
        "result": 657710.331702,
    }
    response.status_code = 200
    assert get_transaction_amount(transaction_usd) == 657710.331702
    url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37"
    headers = {"apikey": API_KEY}
    mock_get.assert_called_once_with("GET", url, headers=headers)


# проверяем код на отрицательный исход при использовании иностранной валюты
@patch("requests.request")
def test_get_transaction_amount_usd_invalid(
    mock_get: Any, transaction_usd: dict[str, int | str | dict[str, str | dict[str, str]]]
) -> None:
    response = mock_get.return_value
    response.json.return_value = {"message": "Not Found"}
    response.status_code = 404
    assert (
        get_transaction_amount(transaction_usd)
        == "Запрос не был успешным.\nКод ошибки: 404.\nОписание ошибки: {'message': 'Not Found'}."
    )
    url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37"
    headers = {"apikey": API_KEY}
    mock_get.assert_called_once_with("GET", url, headers=headers)
