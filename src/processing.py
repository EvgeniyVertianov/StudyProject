def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному
    значению ('EXECUTED' или 'CANCELED') по умолчанию 'EXECUTED'."""
    new_data = list()
    for item in data:
        if item.get("state") == state:
            new_data.append(item)
    return new_data


def sort_by_date(data: list, reverse: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание) и возвращает новый
    список отсортированный по дате (date)."""
    for item in data:
        date = item.get("date")
        if len(date) > 26 or len(date) < 26:
            raise ValueError("Неверный формат даты")
    return sorted(data, key=lambda value: value.get("date"), reverse=reverse)
