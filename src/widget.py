from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Функция принимает строку, содержащую тип и номер карты или счета и возвращает
    замаскированный счет или номер карты."""
    new_data = data.split()
    # проверяем является ли номер, номером карты
    if len(new_data[-1]) == 16:
        new_data[-1] = get_mask_card_number(new_data[-1])
        return " ".join(new_data)
    # проверяем является ли номер, номером счета
    elif len(new_data[-1]) == 20:
        new_data[-1] = get_mask_account(new_data[-1])
        return " ".join(new_data)
    # проверяем на корректность введенного номера карты/счета
    else:
        if "Счет" in data or "счет" in data:
            return get_mask_account(new_data[-1])
        else:
            return get_mask_card_number(new_data[-1])


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку
    с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))
