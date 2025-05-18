import pytest

from src.masks import get_mask_account, get_mask_card_number


# проверка положительного исхода
@pytest.mark.parametrize(
    "correct_data, expected",
    [("1596837868705199", "1596 83** **** 5199"), ("6831982476737658", "6831 98** **** 7658")],
)
def test_get_mask_card_number(correct_data: str, expected: str) -> None:
    assert get_mask_card_number(correct_data) == expected


# проверка ввода некорректных данных
@pytest.mark.parametrize(
    "incorrect_data, expected",
    [
        ("15968378687051990000", "Вы ввели неверное количество цифр карты"),
        ("6831982476", "Вы ввели неверное количество цифр карты"),
        ("", "Вы ввели неверное количество цифр карты"),
    ],
)
def test_get_mask_card_number_invalid_number(incorrect_data: str, expected: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(incorrect_data)
    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == expected


# проверка положительного исхода
@pytest.mark.parametrize(
    "correct_data, expected", [("35383033474447895560", "**5560"), ("73654108430135874305", "**4305")]
)
def test_get_mask_account(correct_data: str, expected: str) -> None:
    assert get_mask_account(correct_data) == expected


# проверка ввода некорректных данных
@pytest.mark.parametrize(
    "incorrect_data, expected",
    [
        ("353830334744478955600000", "Вы ввели неверное количество цифр счета"),
        ("7365410843013587", "Вы ввели неверное количество цифр счета"),
        ("", "Вы ввели неверное количество цифр счета"),
    ],
)
def test_get_mask_account_invalid_number(incorrect_data: str, expected: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(incorrect_data)
    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == expected
