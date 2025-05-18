import os
from typing import Any

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()
# импортируем API_KEY из .env-файла
API_KEY = os.getenv("API_KEY")


def get_transaction_amount(transaction: dict) -> Any:
    """Функция принимает транзакцию и возвращает ее сумму. Если в транзакции валюта не является рублями,
    то функция конвертирует ее в рубли"""
    # получение суммы транзакции по ключу "amount"
    amount = transaction["operationAmount"]["amount"]
    # получение кода валюты по ключу "code"
    currency = transaction["operationAmount"]["currency"]["code"]
    # валюта в которую будет производиться конвертация - рубли
    currency_rub = "RUB"

    # ели код транзакции не рубль то обращаемся к конвертации валюты в рубли
    if currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_rub}&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url, headers=headers)
        status_code = response.status_code
        result = response.json()
        print(result)
        if status_code == 200:
            return result["result"]
        else:
            return f"Запрос не был успешным.\nКод ошибки: {status_code}.\nОписание ошибки: {result}."
    else:
        return amount
