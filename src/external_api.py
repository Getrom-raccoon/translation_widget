import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")


API_KEY = os.getenv("API_KEY")


def conversion_of_amount(transaction):
    """
    Функция  принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    :param transaction: транзакция
    :return: сумма в рублях
    """

    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount")
    currency_code = operation_amount.get("currency", {}).get("code")

    if not amount_str or not currency_code:
        return "Ошибка: недостаточно данных"

    try:
        amount_float = float(amount_str)
    except ValueError:
        return "Ошибка: некорректная сумма"

    if currency_code.upper() == "RUB":
        return amount_float

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount_float}"
    headers = {"apikey": API_KEY}

    conversion = requests.get(url, headers=headers)
    if conversion.status_code == 200:
        data = conversion.json()
        converted_amount = data.get("result")
        return float(converted_amount)
    else:
        return f"Ошибка: {conversion.status_code}, {conversion.text}"
