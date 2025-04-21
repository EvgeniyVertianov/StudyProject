from typing import Union

import pytest


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX,
    где X — это цифра номера."""
    nums_in_number_card = 16
    str_card_number = str(card_number)

    if nums_in_number_card != len(str_card_number):
        raise ValueError("Вы ввели неверное количество цифр карты")
    else:
        return f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[12:16]}"


@pytest.fixture
def value_card():
    return "7000792289606361"


def test_get_mask_card_number(value_card):
    assert get_mask_card_number(value_card) == "7000 79** **** 6361"


def test_get_mask_card_number_invalid_number_more_numbers():
    with pytest.raises(ValueError):
        get_mask_card_number("7000792289606361000")


def test_get_mask_card_number_invalid_number_fewer_numbers():
    with pytest.raises(ValueError):
        get_mask_card_number("70007922")


def test_get_mask_card_number_invalid_number_none_number():
    with pytest.raises(ValueError):
        get_mask_card_number("")


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в формате **ХХХХ,
    где ХХХХ последние четыре цифры."""
    nums_in_account_number = 20
    str_account_number = str(account_number)

    if nums_in_account_number != len(str_account_number):
        raise ValueError("Вы ввели неверное количество цифр счета")
    else:
        return f"**{str_account_number[-4:]}"


@pytest.fixture
def value_account():
    return "73654108430135874305"


def test_get_mask_account(value_account):
    assert get_mask_account(value_account) == "**4305"


def test_get_mask_account_invalid_number_more_numbers():
    with pytest.raises(ValueError):
        get_mask_account("73654108430135874305000")


def test_get_mask_account_invalid_number_fewer_numbers():
    with pytest.raises(ValueError):
        get_mask_account("73654")


def test_get_mask_account_invalid_number_none_number():
    with pytest.raises(ValueError):
        get_mask_account("")
