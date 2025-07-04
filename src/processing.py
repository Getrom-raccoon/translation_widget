def filter_by_state(bill_details: dict, state: str = "EXECUTED") -> list:
    """
    Фильтрует список словарей по указанному состоянию операции.

    Аргументы:
        bill_details (dict): Словарь с деталями банковских операций.
        state (str): Состояние операции для фильтрации (по умолчанию "EXECUTED").

    Возвращает:
        list: Список элементов из bill_details, где значение ключа "state" соответствует указанному state.
    """
    return [i for i in bill_details if i["state"] == state]


def sort_by_date(bill_details: dict, date_sort: bool = True) -> list:
    """
    Сортирует список словарей по дате операции.

    Аргументы:
        bill_details (dict): Словарь с деталями банковских операций.
        date_sort (bool): Флаг, определяющий порядок сортировки:
            - True: Сортировка по убыванию (новые операции в начале).
            - False: Сортировка по возрастанию (старые операции в начале).

    Возвращает:
        list: Отсортированный список словарей с деталями операций.
    """
    return sorted(bill_details, key=lambda d: d["date"], reverse=date_sort)
