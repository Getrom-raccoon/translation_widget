import json
from pathlib import Path


def financial_transaction(path_to_file):
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path_to_file: путь до .json-файла
    :return: список словарей с данными о финансовых транзакциях
    """
    file_path = Path(path_to_file)
    try:
        if not file_path.exists():
            return []
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, PermissionError):
        return []
