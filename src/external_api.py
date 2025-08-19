from http.client import responses
from os import remove

import requests
import os
from dotenv import load_dotenv
load_dotenv('.env')


API_KEY = os.getenv('API_KEY')

def conversion_of_amount(transaction):
    '''
    Функция  принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    :param transaction: транзакция
    :return: сумма в рублях
    '''

    key_amount = [i['operationAmount']['amount'] for i in transaction if i['operationAmount']['amount'] != ""]
    amount_float = float(key_amount[0])
    code_currency = [i['operationAmount']['currency']['code'] for i in transaction if i['operationAmount']['currency']['code'] != ""]
    currency_str = str(code_currency[0])


    if currency_str == 'RUB':
        return f'{amount_float} RUB'

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_str}&amount={amount_float}"

    headers = {'apikey': API_KEY}
    conversion = requests.get(url, headers=headers)

    if conversion.status_code == 200:
        data = conversion.json()
        converted_amount = data.get('result')
        return f'{amount_float} {currency_str} = {round(converted_amount, 2)} RUB'
    else:
        return f'Ошибка: {conversion.status_code}, {conversion.text}'

print(conversion_of_amount([
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]))





