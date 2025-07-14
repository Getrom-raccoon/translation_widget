def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    # Проверяем, содержит ли строка хотя бы одну букву
    if any(i.isalpha() for i in card_number):
        return f"номер карты должен состоять только из цифр"

    # Проверяем длину строки
    if len(card_number) != 16:
        return f"Не соответствующая длина карты (16 цифр)"

    # Если все проверки пройдены, возвращаем маску
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    # Проверяем, содержит ли строка хотя бы одну букву
    if any(i.isalpha() for i in account_number):
        return f"номер счета должен состоять только из цифр"

    # Проверяем длину строки
    if len(account_number) != 20:
        return f"Не соответствующая длина счета (20 цифр)"

    # Если все проверки пройдены, возвращаем маску
    return f"**{account_number[-4:]}"
