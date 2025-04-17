def deffilter_by_state(data: list, status: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному
    значению (по умолчанию 'EXECUTED')."""
    new_data = list()

    for item in data:
        state = item.get("state")
        if state == status and state not in new_data:
            new_data.append(item)
    return new_data


if __name__ == "__main__":
    print(
        deffilter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )


def sort_by_date(data: list) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание) и возвращает новый
    список отсортированный по дате (date)."""
    return sorted(data, key=lambda item: item.get("date"), reverse=True)


if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
