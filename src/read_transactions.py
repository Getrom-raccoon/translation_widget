import pandas as pd


def read_csv_transactions(file_patch):
    """
    Функция считывает финансовые операции из CSV-файла и возвращает список словарей.
    :param file_patch: Путь к CSV-файлу
    :return: список словарей
    """
    df = pd.read_csv(file_patch)
    return df.to_dict(orient="records")


def read_excel_transactions(file_patch):
    """
    Функция считывает финансовые операции из EXCEL-файла и возвращает список словарей.
    :param file_patch: Путь к EXCEL-файлу
    :return: список словарей
    """
    df = pd.read_excel(file_patch)
    return df.to_dict(orient="records")
