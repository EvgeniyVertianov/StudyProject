import unittest
from typing import Any
from unittest.mock import Mock, patch

from src.filters import counting_categories, filter_by_state_v2


# тест функции filter_by_state_v2
# проверяем код на положительный и отрицательный исход
class TestFilterByStateV2(unittest.TestCase):
    @patch("builtins.input", side_effect=["LOAD", "EXECUTED"])
    @patch("builtins.print")
    def test_filter_by_state_v2_invalid_then_valid(self, mock_print: Mock, mock_input: Mock) -> None:
        data_filters = [
            {"description": "Transaction 1", "state": "EXECUTED"},
            {"description": "Transaction 2", "state": "PENDING"},
            {"description": "Transaction 3", "state": "EXECUTED"},
            {"description": "Transaction 4", "state": "CANCELED"},
        ]

        # Вызываем функцию, которую тестируем
        result = filter_by_state_v2(data_filters)

        # Проверяем, что print вызвался с сообщением об ошибке
        mock_print.assert_any_call('Статус операции "LOAD" недоступен')

        # Проверяем, что функция в итоге вернула результат с валидным статусом
        executed_found = False
        for item in result:
            if item["state"] == "EXECUTED":
                executed_found = True
                break  # Достаточно найти хотя бы один "EXECUTED"

        self.assertTrue(executed_found, "Не найден ни один элемент со статусом 'EXECUTED'")


# тест функции filter_by_state_v2
# тест на положительный исход
def test_counting_categories(data_filters: list) -> Any:
    categories = ["Перевод организации", "Открытие вклада", "Перевод с карты на счет", "Перевод с карты на карту"]
    result = counting_categories(data_filters, categories)
    expected = {
        "Перевод организации": 1,
        "Открытие вклада": 1,
        "Перевод с карты на счет": 1,
        "Перевод с карты на карту": 1,
    }
    assert result == expected
