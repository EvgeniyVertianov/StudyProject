from collections import Counter


def filter_by_state_v2(data: list[dict]) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска после чего возвращает
    список словарей, у которых в описании есть данная строка"""
    text = """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: """
    new_list = []
    user_input = input(text)
    while True:
        if user_input.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Статус операции "{user_input}" недоступен')
            user_input = input(text)
        else:
            for item in data:
                state_value = item.get("state")
                if state_value is not None and state_value.upper() == user_input.upper():
                    new_list.append(item)
            print(f'Операции отфильтрованы по статусу "{user_input.upper()}"')
            return new_list


def counting_categories(data: list, categories_of_operations: list) -> str | dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    после чего возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    new_list = []
    for item in data:
        item = item.get("description")
        if item in categories_of_operations:
            new_list.append(item)
    result = dict(Counter(new_list))
    return result


#
#
# transact = [
#     {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589",
#     },
#     {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589",
#     },
#     {
#         "id": 594226727,
#         "state": "CANCELED",
#         "date": "2018-09-12T21:27:25.241689",
#         "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Visa Platinum 1246377376343588",
#         "to": "Счет 14211924144426031657",
#     },
#     {
#         "id": 939719570,
#         "state": "PENDING",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 939719570,
#         "state": "PENDING",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 558167602,
#         "state": "EXECUTED",
#         "date": "2019-04-12T17:27:27.896421",
#         "operationAmount": {"amount": "43861.89", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 73654108430135874305",
#         "to": "Счет 89685546118890842412",
#     },
#     {
#         "id": 407169720,
#         "state": "EXECUTED",
#         "date": "2018-02-03T14:52:08.093722",
#         "operationAmount": {"amount": "67011.26", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод с карты на карту",
#         "from": "MasterCard 4047671689373225",
#         "to": "Maestro 3806652527413662",
#     },
# ]
#
#
# if __name__ == "__main__":
#     print(filter_by_state_v2(transact))
# if __name__ == "__main__":
#     categories_of_operations = [
#         'Перевод организации',
#         'Перевод с карты на карту',
#         'Перевод с карты на счет',
#         'Перевод со счета на счет',
#         'Открытие вклада'
#     ]
#     print(counting_categories(transact, categories_of_operations))
