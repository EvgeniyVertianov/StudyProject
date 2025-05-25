import csv
from typing import Any
from unittest import mock

import pandas as pd

from src.readers import reader_csv_file, reader_xlsx_file


# проверяем код на положительный исход
def test_reader_csv_file(correct_path_to_csv: str) -> None:
    with open(correct_path_to_csv) as file:
        reader = csv.DictReader(file, delimiter=";")
        result = []
        for row in reader:
            result.append(row)
    assert reader_csv_file(correct_path_to_csv) == result


def test_reader_xlsx_file(correct_path_to_xlsx: str) -> None:
    data = pd.read_excel(correct_path_to_xlsx, dtype=str)
    result = data.to_dict(orient="records")
    assert reader_xlsx_file(correct_path_to_xlsx) == result


# проверяем код на отрицательный исход
@mock.patch("builtins.open", side_effect=FileNotFoundError)
def test_reader_csv_file_invalid(mock_open: Any) -> None:
    result = reader_csv_file("fake_path.csv")
    assert result == []


@mock.patch("builtins.open", side_effect=FileNotFoundError)
def test_reader_xlsx_file_invalid(mock_open: Any) -> None:
    result = reader_xlsx_file("fake_path.xlsx")
    assert result == []
