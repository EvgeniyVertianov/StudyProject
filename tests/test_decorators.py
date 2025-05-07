import pytest

from src.decorators import log


@log()
def function_sum_for_test(x, y):
    return x + y


@log()
def function_division_for_test(x, y):
    return x / y


# тесты для успешного выполнения
def test_success_sum(capsys):
    function_sum_for_test(1, 3)
    captured = capsys.readouterr()
    assert captured.out == "function_sum_for_test ok\n\n"


def test_success_division(capsys):
    function_division_for_test(1, 3)
    captured = capsys.readouterr()
    assert captured.out == "function_division_for_test ok\n\n"


# тесты для ошибки
def test_log_exception():
    with pytest.raises(Exception, match=""):
        function_sum_for_test()


def test_log_sum_error(capsys):
    with pytest.raises(TypeError):
        function_sum_for_test("1", 3)
    captured = capsys.readouterr()
    assert captured.out == "function_sum_for_test error: <class 'TypeError'>. Inputs: ('1', 3), {}\n\n"


def test_log_division_error(capsys):
    with pytest.raises(ZeroDivisionError):
        function_division_for_test(4, 0)
    captured = capsys.readouterr()
    assert captured.out == "function_division_for_test error: <class 'ZeroDivisionError'>. Inputs: (4, 0), {}\n\n"
