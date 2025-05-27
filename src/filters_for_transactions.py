import re


def filter_by_state_v2(data: list, user_input: str = "EXECUTED") -> str:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска после чего возвращает
    список словарей, у которых в описании есть данная строка"""
    text = """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: """
    new_list = []
    user_input = input(text)
    while True:
        if user_input not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Статус операции "{user_input}" недоступен')
            user_input = input(text)
        for item in data:
            if re.findall(user_input, item["state"], flags=re.IGNORECASE):
                new_list.append(item)
        return f'Операции отфильтрованы по статусу "{user_input}"\n{new_list}'


def counting_categories():
    pass


if __name__ == "__main__":
    transact = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 939719570,
            "state": "PENDING",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719570,
            "state": "PENDING",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]

    print(filter_by_state_v2(transact))
