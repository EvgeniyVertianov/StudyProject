import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers import reader_csv_file, reader_xlsx_file
from src.search import search_string
from src.utils import get_info_about_transactions
from src.widget import get_date, mask_account_card

PATH_TO_FILES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

def select_category() -> list[dict]:
    """Функция для выбора файла и чтения данных об операциях"""
    while True:
        menu = ["JSON-файл", "CSV-файл", "XLSX-файл"]
        text = """
            Привет! Добро пожаловать в программу работы с банковскими транзакциями.
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла
            """
        print(text)
        try:
            user_input = int(input("Поле ввода: "))
            print(f"Для обработки выбран {menu[user_input - 1]}.")
            if user_input == 1:
                data = get_info_about_transactions(os.path.join(PATH_TO_FILES, "operations.json"))
                return data
            elif user_input == 2:
                data = reader_csv_file(os.path.join(PATH_TO_FILES, "transactions.csv"))
                return data
            elif user_input == 3:
                data = reader_xlsx_file(os.path.join(PATH_TO_FILES, "transactions_excel.xlsx"))
                return data
            else:
                print("Выбран несуществующий пункт меню. Пожалуйста, выберите пункт из предложенного списка.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
        except IndexError:
            print("Выбран несуществующий пункт меню. Пожалуйста, выберите пункт из предложенного списка (1-3).")

def choose_category_filter(list_of_transactions: list[dict]) -> list[dict]:
    """Функция для выбора фильтрации по статусу"""
    available_status = ["executed", "canceled", "pending"]
    while True:
        user_choose_category = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.\n\nПоле ввода: """
        ).lower()
        if user_choose_category in available_status:
            result = filter_by_state(list_of_transactions, user_choose_category.upper())
            if result:
                return result
            else:
                print("Операции по данному статусу отсутствуют")
        else:
            print(f"Статус операции {user_choose_category} недоступен")
            continue
    return [{}]



def choose_params_for_date(list_of_transactions: list[dict]) -> list[dict]:
    """Функция для выбора сортировки даты"""
    while True:
        date_input = input("Отсортировать операции по дате? Да/Нет.\nПоле ввода: ").lower()
        if date_input == "нет":
            return list_of_transactions
        elif date_input == "да":
            while True:
                sort_input = input("Отсортировать по возрастанию или по убыванию? В/У.\nПоле ввода: ").lower()
                if sort_input == "в":
                    return sort_by_date(list_of_transactions, False)
                elif sort_input == "у":
                    return sort_by_date(list_of_transactions, True)
                else:
                    print("Введите пожалуйста корректное значение ('В' или 'У').")
        else:
            print("Введите пожалуйста корректное значение ('Да' или 'Нет').")

def choose_rub(list_of_transactions: list[dict]) -> list[dict]:
    """Функция для выбора вывода всех операций или только рублевых операций"""
    while True:
        user_rub_input = input("Выводить только рублевые транзакции? Да/Нет.\nПоле ввода: ").lower()
        if user_rub_input == "нет":
            return list_of_transactions
        elif user_rub_input == "да":
            try:
                return list(filter_by_currency(list_of_transactions, "RUB"))
            except ValueError:
                print("Операции по данной валюте отсутствуют")
        else:
            print("Введите пожалуйста корректное значение ('Да' или 'Нет').")

def choose_search(list_of_transactions: list[dict]) -> list[dict]:
    """Функция для выбора фильтрации по слову"""
    while True:
        user_search_input = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет. \nПоле ввода: "
        ).lower()
        if user_search_input == "нет":
            return list_of_transactions
        elif user_search_input == "да":
            user_word = input("Введите пожалуйста слово в описании операции для поиска.\nПоле ввода: ").lower()
            return search_string(list_of_transactions, user_word)
        else:
            print("Введите пожалуйста корректное значение ('Да' или 'Нет').")

def main() -> None:
    """Функция, описывающая всю логику работы приложения"""

    transactions = select_category()
    filtered_transaction = choose_category_filter(transactions)
    transactions_sorted = choose_params_for_date(filtered_transaction)
    transactions_rub_sorted = choose_rub(transactions_sorted)
    final_result = choose_search(transactions_rub_sorted)

    print("Программа: Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(final_result)}")

    for transaction in final_result:
        date = get_date(transaction["date"])
        amount = transaction["amount"] if "amount" in transaction else transaction["operationAmount"]["amount"]
        from_transaction = mask_account_card(transaction.get("from", ""))
        to_transaction = mask_account_card(transaction.get("to", ""))
        description = transaction["description"]
        currency_code = (
            transaction["currency_code"]
            if "currency_code" in transaction
            else transaction["operationAmount"]["currency"]["name"]
        )
        print(f"{date} {description}\n{from_transaction} -> {to_transaction}\nСумма: {amount} {currency_code}\n\n")

if __name__ == "__main__":
    main()
