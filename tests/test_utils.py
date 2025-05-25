import json
from typing import Any
from unittest import mock

from src.utils import get_info_about_transactions


# проверяем код на положительный исход
def test_get_info_about_transactions(correct_path_to_json: str) -> None:
    with open(correct_path_to_json) as file:
        data = json.load(file)
    assert get_info_about_transactions(correct_path_to_json) == data


# проверяем код на отрицательный исход
def test_get_info_about_transactions_invalid(incorrect_path_to_json: str) -> None:
    assert get_info_about_transactions(incorrect_path_to_json) == []


@mock.patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_open: Any) -> None:
    result = get_info_about_transactions("fake_path.json")
    assert result == []


@mock.patch("builtins.open", new_callable=mock.mock_open, read_data="invalid json")
@mock.patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load: Any, mock_open: Any) -> None:
    result = get_info_about_transactions("fake_path.json")
    assert result == []
