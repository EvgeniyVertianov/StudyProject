def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX,
    где X — это цифра номера."""
    nums_in_number_card = 16
    str_card_number = str(card_number)

    if nums_in_number_card != len(str_card_number):
        raise ValueError("Вы ввели неверное количество цифр карты")
    else:
        return f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[12:16]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в формате **ХХХХ,
    где ХХХХ последние четыре цифры."""
    nums_in_account_number = 20
    str_account_number = str(account_number)

    if nums_in_account_number != len(str_account_number):
        raise ValueError("Вы ввели неверное количество цифр счета")
    else:
        return f"**{str_account_number[-4:]}"
