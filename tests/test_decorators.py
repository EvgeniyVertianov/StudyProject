from typing import Any

import pytest

from src.decorators import log


@log()
def function_sum_for_test(x: int, y: int) -> float:
    return x + y


@log()
def function_division_for_test(x: int, y: int) -> float:
    return x / y


# тесты для успешного выполнения
def test_success_sum(capsys: Any) -> None:
    function_sum_for_test(1, 3)
    captured = capsys.readouterr()
    assert captured.out == "function_sum_for_test ok\n\n"


def test_success_division(capsys: Any) -> None:
    function_division_for_test(1, 3)
    captured = capsys.readouterr()
    assert captured.out == "function_division_for_test ok\n\n"


# тесты для ошибки
def test_log_exception() -> None:
    with pytest.raises(Exception, match=""):
        function_sum_for_test()


def test_log_sum_error(capsys: Any) -> None:
    with pytest.raises(TypeError):
        function_sum_for_test("1", 3)
    captured = capsys.readouterr()
    assert captured.out == "function_sum_for_test error: <class 'TypeError'>. Inputs: ('1', 3), {}\n\n"


def test_log_division_error(capsys: Any) -> None:
    with pytest.raises(ZeroDivisionError):
        function_division_for_test(4, 0)
    captured = capsys.readouterr()
    assert captured.out == "function_division_for_test error: <class 'ZeroDivisionError'>. Inputs: (4, 0), {}\n\n"
