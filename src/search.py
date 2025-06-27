import re


def search_string(transactions_list: list[dict], string: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""

    return [
        transaction
        for transaction in transactions_list
        if re.search(string.lower(), transaction["description"].lower())
    ]
