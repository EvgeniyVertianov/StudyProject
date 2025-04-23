import pytest


# фикстуры к модулю processing
# общие фикстуры на функции filter_by_state, sort_by_date
@pytest.fixture
def data_processing():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# фикстуры к функции filter_by_state без ключа "state"
@pytest.fixture
def empty_state_filter_by_state():
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


# фикстуры к функции filter_by_state с иными значениями "state"
@pytest.fixture
def different_state_filter_by_state():
    return [
        {"id": 41428829, "state": "ACTIVE", "date": "2019-07-03T18:35:29.512364"},
        {"id": 41428570, "state": "ACTIVE", "date": "2021-08-04T18:35:29.512364"},
        {"id": 939719570, "state": "DENIED", "date": "2019-06-14T03:09:59.435572"},
        {"id": 939719556, "state": "DENIED", "date": "2019-09-15T02:08:58.425572"},
    ]


# фикстуры к функции sort_by_date на сортировку одинаковых дат
@pytest.fixture
def identical_dates():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]
