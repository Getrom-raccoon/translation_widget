import re


def process_bank_search(data, search):
    """
    функция принимает список словарей с данными о банковских операциях и строку поиска,
    и возвращает список словарей, у которых в описании есть данная строка.
    :param data: список словарей с данными о банковских операциях
    :param search: строка поиска
    :return: возвращает список словарей, у которых в описании есть данная строка
    """
    pattern = re.compile(search, re.IGNORECASE)

    result = []
    for item in data:
        if isinstance(item, dict):
            found = False
            for value in item.values():
                if isinstance(value, (str, int, float)):
                    text_value = str(value)
                    if pattern.search(text_value):
                        found = True
                        break
                elif isinstance(value, list):
                    for elem in value:
                        if isinstance(elem, (str, int, float)):
                            if pattern.search(str(elem)):
                                found = True
                                break
                        elif isinstance(elem, dict):
                            if any(pattern.search(str(v)) for v in elem.values()):
                                found = True
                                break
                elif isinstance(value, dict):
                    if any(pattern.search(str(v)) for v in value.values()):
                        found = True
                        break

            if found:
                result.append(item)

    return result
