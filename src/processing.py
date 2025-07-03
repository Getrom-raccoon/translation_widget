def filter_by_state(bill_details: dict, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и возвращает списки опционально значения для ключа state"""
    return [i for i in bill_details if i["state"] == state]


def sort_by_date(bill_details: dict, date_sort: bool = True) -> list:
    """функция принимает список словарей и возвращает его в заданном порядке по дате"""
    return sorted(bill_details, key=lambda d: d["date"], reverse=date_sort)
