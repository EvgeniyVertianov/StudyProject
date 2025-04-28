import pytest

from src.processing import filter_by_state, sort_by_date


# тест функции filter_by_state
def test_filter_by_state(data_processing):
    # state по умолчанию "EXECUTED"
    assert filter_by_state(data_processing) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    # state "CANCELED"
    assert filter_by_state(data_processing, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# тест функции filter_by_state на отсутствие ключа "state"
def test_filter_by_state_empty_status(empty_state_filter_by_state):
    assert filter_by_state(empty_state_filter_by_state) == []


# тест функции filter_by_state на иные значения "state"
@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "ACTIVE",
            [
                {"id": 41428829, "state": "ACTIVE", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428570, "state": "ACTIVE", "date": "2021-08-04T18:35:29.512364"},
            ],
        ),
        (
            "DENIED",
            [
                {"id": 939719570, "state": "DENIED", "date": "2019-06-14T03:09:59.435572"},
                {"id": 939719556, "state": "DENIED", "date": "2019-09-15T02:08:58.425572"},
            ],
        ),
    ],
)
def test_filter_by_state_different_state(different_state_filter_by_state, state, expected):
    assert filter_by_state(different_state_filter_by_state, state) == expected


# тест функции sort_by_date на сортировку в порядке убывания и возрастания
@pytest.mark.parametrize(
    "reverse, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(data_processing, reverse, expected):
    assert sort_by_date(data_processing, reverse) == expected


# тест функции sort_by_date на корректность сортировки при одинаковых датах
def test_sort_by_date_identical_dates(identical_dates):
    # reverse по умолчанию "True"
    assert sort_by_date(identical_dates) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


# тест функции sort_by_date на неверный формат даты
def test_sort_by_date_incorrect_date():
    with pytest.raises(ValueError) as exc_info:
        sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.51236"}])
    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == "Неверный формат даты"
