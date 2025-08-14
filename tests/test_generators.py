import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
]

@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("руб.", [873106923, 594226727]),
        ("EUR", []),
        ("", []),
        (None, []),
        ("RUB", []),
    ]
)
def test_filter_by_currency(currency, expected_ids):
    result = list(filter_by_currency(transactions, currency))
    result_ids = [t["id"] for t in result]
    assert result_ids == expected_ids

def test_filter_by_currency_empty_transactions():
    empty_transactions = []
    result = list(filter_by_currency(empty_transactions, "USD"))
    assert result == []

def test_filter_by_currency_no_currency_field():
    transactions_without_currency = [
        {"descriptoin": "No currency field"}
    ]
    result = list(filter_by_currency(transactions_without_currency, "USD"))
    assert result == []

@pytest.mark.parametrize(
    "input_transactions, expected_descriptions",
    [
        (transactions, [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации"
        ]),
        ([], []),
        ([{"description": "Test"}], ["Test"]),
        ([{"id": 1}, {"description": ""}], [""]),
        ([{"description": "A"}, {"description": "B"}], ["A", "B"]),
    ]
)
def test_transaction_descriptions(input_transactions, expected_descriptions):
    result = list(transaction_descriptions(input_transactions))
    assert result == expected_descriptions

@pytest.mark.parametrize(
    "x, y, expected_numbers",
    [
        (1000, 1005, ["0000 0000 0000 1000", "0000 0000 0000 1001", "0000 0000 0000 1002",
                      "0000 0000 0000 1003", "0000 0000 0000 1004", "0000 0000 0000 1005"]),
        (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
        (1234, 1234, ["0000 0000 0000 1234"]),
        (0, 0, ["0000 0000 0000 0000"]),
    ]
)
def test_card_number_generator(x, y, expected_numbers):
    result = list(card_number_generator(x, y))
    assert result == expected_numbers

def test_card_number_generator_invalid_range():
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(10, 5))
        assert str(exc_info.value) == "Минимальное значение диапазона не может быть больше максимального"

def test_cart_number_generator_edge_cases():
    result = list(card_number_generator(0, 9999))
    assert len(result) == 10000
    assert result[0] == "0000 0000 0000 0000"
    assert result[-1] == "0000 0000 0000 9999"