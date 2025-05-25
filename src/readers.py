import csv

import pandas as pd


def reader_csv_file(path_to_file: str) -> list | str:
    """Функция принимает путь к csv файлу и открывает его"""
    try:
        with open(path_to_file) as file:
            reader = csv.DictReader(file, delimiter=";")
            result = []
            for row in reader:
                result.append(row)
            return result
    except FileNotFoundError as info:
        print(f"Произошла ошибка: {type(info)}\n{info}")
        return []


def reader_xlsx_file(path_to_file: str) -> list:
    """Функция принимает путь к xlsx файлу и открывает его"""
    try:
        data = pd.read_excel(path_to_file, dtype=str)
        result = data.to_dict(orient="records")
        return result
    except FileNotFoundError as info:
        print(f"Произошла ошибка: {type(info)}\n{info}")
        return []


# if __name__ == "__main__":
#     print(reader_csv_file("/Users/vertianovev/Учеба/Code/StudyProject/data/transactions.csv"))
#
# if __name__ == "__main__":
#     print(reader_xlsx_file("/Users/vertianovev/Учеба/Code/StudyProject/data/transactions_excel.xlsx"))
