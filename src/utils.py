import json


def financial_transaction(path_to_file):
    '''
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path_to_file: путь до .json-файла
    :return: список словарей с данными о финансовых транзакциях
    '''
    try:
        with open(f'../{path_to_file}', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError or json.JSONDecodeError:
        return {}
# print(financial_transaction('data/operations.json'))