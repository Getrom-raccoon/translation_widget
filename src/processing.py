def filter_by_state(bill_details: dict, state: str = "EXECUTED") -> list or str:
    """
    Фильтрует список словарей по указанному состоянию операции.

    Аргументы:
        bill_details (dict): Словарь с деталями банковских операций.
        state (str): Состояние операции для фильтрации (по умолчанию "EXECUTED").

    Возвращает:
        list: Список элементов из bill_details, где значение ключа "state" соответствует указанному state.
    """
    filter_bill =  [i for i in bill_details if i["state"] == state]
    if filter_bill == []:
        return f"нет данных"
    else:
        return filter_bill


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
    for details in bill_details:
        if "date" not in details:
            for i in details:
                if "date" not in i:
                    return f"некорректный ввод"
    return sorted(bill_details, key=lambda d: d["date"], reverse=date_sort)

