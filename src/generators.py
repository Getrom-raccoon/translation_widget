def filter_by_currency(transactions, currency):
    """
    Функция фильтрует список транзакций по указанной валюте.
    :param transactions: Список словарей с транзакциями.
    :param currency: тип валюты
    :return: интератор, который возвращает транзакцию по валюте.
    """
    for transaction in transactions:
        if (
                "operationAmount" in transaction and "currency" in transaction["operationAmount"] and "name" in
                transaction["operationAmount"]["currency"]
        ):
            if transaction["operationAmount"]["currency"]["name"] == currency:
                yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    :param transactions: Список словарей с транзакциями.
    :return: описание каждой операции по очереди.
    """
    for spending in transactions:
        yield spending["description"]