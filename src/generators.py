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
