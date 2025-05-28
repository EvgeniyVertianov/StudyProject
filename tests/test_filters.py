from typing import Any
from unittest.mock import Mock, patch

from src.filters import counting_categories, filter_by_state_v2


# тест функции filter_by_state_v2
# проверяем код на положительный и отрицательный исход
@patch("builtins.input", side_effect=["LOAD", "EXECUTED"])
@patch("builtins.print")
def test_filter_by_state_v2_invalid_then_valid(mock_print: Mock, data_filters: list) -> None:
    result = filter_by_state_v2(data_filters)
    # Проверяем, что print вызвался с сообщением об ошибке
    mock_print.assert_called_with('Статус операции "LOAD" недоступен')
    # Проверяем, что функция в итоге вернула результат с валидным статусом
    assert "EXECUTED" in result


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
