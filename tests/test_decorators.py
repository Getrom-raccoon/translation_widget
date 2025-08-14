import logging
import pytest
import os
from src.decorators import log

@pytest.fixture(autouse=True)
def clear_log_file():
    """Очистка файла логов перед каждым тестом."""
    for file in ["mylog.txt", "error_log.txt"]:
        if os.path.exists(file):
            try:
                os.remove(file)
            except PermissionError:
                pass


def test_successful_execution(capsys):
    """Тест успешного выполнения функции с выводом в консоль."""
    @log()
    def add(x, y):
        return x + y

    result = add(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert "add started" in captured.out
    assert "add ок" in captured.out

def test_exception_handling(capsys):
    """Тест обработки исключения."""

    @log()
    def faulty_function():
        raise ValueError("Something went wrong")

    with pytest.raises(ValueError) as exc_info:
        faulty_function()

    captured = capsys.readouterr()
    assert "faulty_function started" in captured.out
    assert "faulty_function error: ValueError. Inputs: (), {}" in captured.out

def test_logging_to_file():
    """Тест логирования в файл."""
    @log(filename="mylog.txt")
    def multiply(x, y):
        return x * y

    multiply(3, 4)

    with open("mylog.txt", "r", encoding="utf-8") as file:
        logs = file.readlines()
        assert "multiply started\n" in logs
        assert "multiply ок\n" in logs

def test_logging_with_exception_to_file():
    """Тест логирования ошибки в файл."""
    @log(filename="error_log.txt")
    def faulty_function():
        raise ValueError("Something went wrong")

    with pytest.raises(ValueError):
        faulty_function()

    with open("error_log.txt", "r") as file:
        logs = file.readlines()
        assert "faulty_function started\n" in logs
        assert "faulty_function error: ValueError. Inputs: (), {}\n" in logs

def test_decorator_preserves_function_metadata():
    """Тест сохранения метаданных функции."""

    @log()
    def sample_function():
        """Простая функция."""
        pass

    assert sample_function.__name__ == "sample_function"

    assert sample_function.__doc__ == "Простая функция."


if __name__ == "__main__":
    pytest.main()