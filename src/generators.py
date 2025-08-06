def filter_by_currency(transactions, currency):
    """
    Функция фильтрует список транзакций по указанной валюте.
    :param transactions: Список словарей с транзакциями.
    :param currency: тип валюты
    :return: интератор, который возвращает транзакцию по валюте.
    """
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and "name" in transaction["operationAmount"]["currency"]
        ):
            if transaction["operationAmount"]["currency"]["name"] == currency:
                yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    :param transactions: Список словарей с транзакциями.
    :return: описание каждой операции по очереди.
    """
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(x, y):
    """
    Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    :param x: минимальное значение диапозона
    :param y: максимальное значение диапозона
    :return: сгенерированный номер карты в формате строки
    """
    if x > y:
        raise ValueError("Минимальное значение диапозона не может быть больше максимального")

    for number in range(x, y + 1):
        number_str = str(10**16 + number)[-16:]
        formatted = " ".join([number_str[i : i + 4] for i in range(0, 16, 4)])
        yield formatted
