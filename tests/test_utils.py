import pytest
import json
from pathlib import Path
from src.utils import financial_transaction

TEST_FILE_PATH = "data/operations.json"


def create_test_json_file(content, filename="test_operations.json"):
    """Создаёт временный JSON-файл с заданным содержимым."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(content))
    return filename


def remove_test_file(filename):
    """Удаляет тестовый файл."""
    if Path(filename).exists():
        Path(filename).unlink()


@pytest.fixture
def setup_teardown():
    """Фикстура для создания и удаления тестовых файлов."""
    yield
    remove_test_file("test_empty.json")
    remove_test_file("test_invalid.json")
    remove_test_file("test_not_list.json")


def test_financial_transaction_valid_file(setup_teardown):
    """файл существует и содержит список транзакций."""
    test_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01",
            "operationAmount": {
                "amount": "100.00",
                "currency": {"name": "руб.", "code": "RUB"}
            },
            "description": "Покупка",
            "from": "Счет 123",
            "to": "Счет 456"
        }
    ]
    filename = create_test_json_file(test_data, "test_operations.json")
    result = financial_transaction(filename)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["id"] == 1
    remove_test_file(filename)


def test_financial_transaction_empty_file(setup_teardown):
    """файл пустой."""
    filename = create_test_json_file([], "test_empty.json")
    result = financial_transaction(filename)
    assert result == []
    remove_test_file(filename)


def test_financial_transaction_invalid_content(setup_teardown):
    """файл содержит не список."""
    invalid_data = {"not_a_list": "value"}
    filename = create_test_json_file(invalid_data, "test_not_list.json")
    result = financial_transaction(filename)
    assert result == []
    remove_test_file(filename)


def test_financial_transaction_nonexistent_file():
    """файл не существует."""
    result = financial_transaction("nonexistent.json")
    assert result == []


def test_financial_transaction_corrupted_json():
    """файл с некорректным JSON."""
    filename = "test_invalid.json"
    with open(filename, 'w') as f:
        f.write("invalid json content")
    result = financial_transaction(filename)
    assert result == []
    remove_test_file(filename)
