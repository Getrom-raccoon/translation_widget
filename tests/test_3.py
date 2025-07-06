def filter_by_state(bill_details: dict, state='EXECUTED') -> dict:
    """Функция принимает список словарей и возвращает списки опционально значения для ключа state"""
    return [i for i in bill_details if i['state'] == state]


print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED'))


def sort_by_date(bill_details: dict, date_sort=True) -> dict:
    """функция принимает список словарей и возвращает его в заданном порядке по дате"""
    return sorted(bill_details, key=lambda d: d['date'], reverse=date_sort)


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], False))
