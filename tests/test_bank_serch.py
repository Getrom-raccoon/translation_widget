import pytest
from src.bank_search import process_bank_search


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "amount": 1000,
            "to": "Счет 12345678901234567890",
            "operationAmount": {"amount": "1000", "currency": {"name": "руб."}},
        },
        {
            "id": 2,
            "description": "Оплата услуг ЖКХ",
            "from": "Visa Platinum 7000792289606361",
            "details": ["Квартплата", "Электричество"],
            "meta": {"category": "utilities", "tags": ["home", "monthly"]},
        },
        {
            "id": 3,
            "description": "Покупка в магазине",
            "merchant": {"name": "Пятёрочка", "location": "Москва"},
            "amount": 599.99,
        },
        {
            "id": 4,
            "description": "Перевод физическому лицу",
            "to": "Maestro 1234567890123456",
            "note": "За подарок",
        },
        {
            "id": 5,
            "description": "Возврат средств",
            "refund_reason": "Товар не подошёл",
            "amount": -850,
        },
    ]


def test_search_in_description(sample_transactions):
    result = process_bank_search(sample_transactions, "перевод")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 4


def test_search_in_nested_dict(sample_transactions):
    result = process_bank_search(sample_transactions, "пятёрочка")
    assert len(result) == 1
    assert result[0]["id"] == 3
    assert result[0]["merchant"]["name"] == "Пятёрочка"


def test_search_in_list(sample_transactions):
    result = process_bank_search(sample_transactions, "электричество")
    assert len(result) == 1
    assert result[0]["id"] == 2
    assert "Электричество" in result[0]["details"]


def test_search_in_numeric_field(sample_transactions):
    result = process_bank_search(sample_transactions, "599.99")
    assert len(result) == 1
    assert result[0]["id"] == 3
    assert result[0]["amount"] == 599.99


def test_case_insensitive_search(sample_transactions):
    result = process_bank_search(sample_transactions, "ПЯТЁРОЧКА")
    assert len(result) == 1
    assert result[0]["id"] == 3


def test_partial_word_search(sample_transactions):
    result = process_bank_search(sample_transactions, "магазин")
    assert len(result) == 1
    assert result[0]["id"] == 3


def test_no_matches(sample_transactions):
    result = process_bank_search(sample_transactions, "несуществующий_поиск")
    assert result == []


def test_empty_transaction_list():
    result = process_bank_search([], "поиск")
    assert result == []
