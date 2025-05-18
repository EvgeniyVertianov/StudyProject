import json
from typing import Any


def get_info_about_transactions(path_to_file: str) -> Any:
    """Функция принимает путь к файлу с транзакциями и открывает его"""
    try:
        with open(path_to_file) as file:
            data = json.load(file)
            return data
    except FileNotFoundError as expect_info:
        print(f"Файл не найден: {expect_info}")
        return []
    except json.JSONDecodeError as expect_info:
        print(f"Ошибка декодирования файла: {expect_info}")
        return []
