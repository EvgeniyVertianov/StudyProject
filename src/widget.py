from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(data: str) -> str:
    """Функция принимает строку, содержащую тип и номер карты или счета и возвращает
    замаскированный счет или номер карты"""
    new_data = data.split()

    if len(new_data[-1]) == 16:  # проверяем является ли номер, номером карты
        new_data[-1] = get_mask_card_number(new_data[-1])
        return " ".join(new_data)
    elif len(new_data[-1]) == 20:  # проверяем является ли номер, номером счета
        new_data[-1] = get_mask_account(new_data[-1])
        return " ".join(new_data)
    else:  # проверяем на корректность введенного номера карты/счета
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
