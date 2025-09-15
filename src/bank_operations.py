import re

def process_bank_operations(data, categories):
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций, 
    и возвращает словарь, в котором ключи - названия категорий, а значения - количество операций в каждой категории.
    :param data: список словарей с данными о банковских операциях
    :param categories: список категорий операций
    :return: словарь, в котором ключи - названия категорий, а значения - количество операций в каждой категории
    """
    result = {}
    for category in categories:
        result[category] = 0

    for item in data:
        if isinstance(item, dict) and 'description' in item:
            description = item['description']
            for category in categories:
                if re.search(rf"\b{re.escape(category)}\b", description):
                    result[category] += 1

    return result

# Данные
bank_operations = [
    {'id': 1, 'description': 'Покупка в магазине "Мир"', 'amount': 500},
    {'id': 2, 'description': 'Перевод на карту друга', 'amount': 1000},
    {'id': 3, 'description': 'Оплата интернета', 'amount': 300},
    {'id': 4, 'description': 'Снятие наличных в банкомате', 'amount': 200},
    {'id': 5, 'description': 'Покупка в аптеке', 'amount': 150}
]

# Список категорий
categories = ["Покупка", "Перевод", "Снятие"]

# Вызов функции
result = process_bank_operations(bank_operations, categories)
print(result)