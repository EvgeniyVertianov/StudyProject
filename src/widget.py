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


def get_date(date: str) -> str:
    """Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку
    с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")."""
    new_date = date[:10]
    month_with_31_days = ("01", "03", "05", "07", "08", "10", "12")
    month_with_30_days = ("04", "06", "09", "11")
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    leap_years = []

    for i in range(1764, 2133, 4):
        leap_years.append(i)

    if year not in leap_years and month == "02" and int(day) > 28:
        raise ValueError("Это не високосный год. В феврале не может быть больше 28 дней")
    if month in month_with_30_days and int(day) > 30:
        raise ValueError("В данном месяце не может быть больше 30 дней")
    elif month in month_with_31_days and int(day) > 31:
        raise ValueError("В данном месяце не может быть больше 31 дня")
    elif len(date) == 0:
        raise ValueError("Вы ничего не ввели")
    elif "-" not in new_date or ":" not in date or "." not in date or "T" not in date:
        raise ValueError("Некорректно указан формат входных данных")
    elif day == "00":
        raise ValueError("День указан неверно")
    elif int(month) > 12 or month == "00":
        raise ValueError("Месяц указан неверно")
    elif int(year) > 9000 or year == "0000":
        raise ValueError("Год указан неверно")
    elif len(date) > 26 or len(date) < 26:
        raise ValueError("Вы ввели неверное количество символов")
    else:
        return f"{day}.{month}.{year}"
