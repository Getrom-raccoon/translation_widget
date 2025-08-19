from unittest.mock import patch, Mock
from src.external_api import conversion_of_amount

TRANSACTION_RUB = {
    "operationAmount": {
        "amount": "31957.58",
        "currency": {"code": "RUB"}
    }
}

TRANSACTION_USD = {
    "operationAmount": {
        "amount": "100.00",
        "currency": {"code": "USD"}
    }
}

TRANSACTION_EUR = {
    "operationAmount": {
        "amount": "50.00",
        "currency": {"code": "EUR"}
    }
}

TRANSACTION_INVALID = {
    "operationAmount": {
        "amount": "",
        "currency": {"code": "RUB"}
    }
}


@patch("src.external_api.requests.get")
def test_conversion_of_amount_rub(mock_get):
    """сумма в RUB не конвертируется."""
    result = conversion_of_amount(TRANSACTION_RUB)
    assert result == 31957.58


@patch("src.external_api.requests.get")
def test_conversion_of_amount_usd_success(mock_get):
    """конвертация USD в RUB, успешный ответ API."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 8500.0}
    mock_get.return_value = mock_response

    result = conversion_of_amount(TRANSACTION_USD)
    assert result == 8500.0


@patch("src.external_api.requests.get")
def test_conversion_of_amount_eur_success(mock_get):
    """конвертация EUR в RUB, успешный ответ API."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.0}
    mock_get.return_value = mock_response

    result = conversion_of_amount(TRANSACTION_EUR)
    assert result == 7500.0


@patch("src.external_api.requests.get")
def test_conversion_of_amount_api_error(mock_get):
    """ошибка при запросе к API."""
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.text = "Unauthorized"
    mock_get.return_value = mock_response

    result = conversion_of_amount(TRANSACTION_USD)
    assert "Ошибка: 401, Unauthorized" in result


@patch("src.external_api.requests.get")
def test_conversion_of_amount_invalid_transaction(mock_get):
    """недостаточно данных в транзакции."""
    result = conversion_of_amount(TRANSACTION_INVALID)
    assert "Ошибка: недостаточно данных" in result


@patch("src.external_api.requests.get")
def test_conversion_of_amount_invalid_amount(mock_get):
    """некорректное значение суммы."""
    invalid_transaction = {
        "operationAmount": {
            "amount": "abc",
            "currency": {"code": "RUB"}
        }
    }
    result = conversion_of_amount(invalid_transaction)
    assert "Ошибка: некорректная сумма" in result