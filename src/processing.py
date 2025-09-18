def filter_by_state(bill_details: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует список словарей по указанному состоянию операции.
    Аргументы:
        bill_details (list): Список словарей с деталями банковских операций.
        state (str): Состояние операции для фильтрации (по умолчанию "EXECUTED").
    Возвращает:
        list: Список элементов из bill_details, где значение ключа "state" соответствует указанному state.
    """
    if not isinstance(bill_details, list):
        return []

    filtered = []
    for item in bill_details:
        if isinstance(item, dict) and "state" in item and item["state"] == state:
            filtered.append(item)

    return filtered if filtered else []


def sort_by_date(bill_details: list, date_sort: bool = True) -> list:
    """
    Сортирует список словарей по дате операции.
    Аргументы:
        bill_details (list): Список словарей с деталями банковских операций.
        date_sort (bool): Флаг, определяющий порядок сортировки:
            - True: Сортировка по убыванию (новые операции в начале).
            - False: Сортировка по возрастанию (старые операции в начале).
    Возвращает:
        list: Отсортированный список словарей с деталями операций.
    """
    if not isinstance(bill_details, list):
        return []

    # Фильтруем только те записи, у которых есть дата
    valid_transactions = [t for t in bill_details if isinstance(t, dict) and "date" in t]

    return sorted(valid_transactions, key=lambda d: d["date"], reverse=date_sort)
