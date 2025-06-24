def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(get_mask_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{get_mask_account[-4:]}"
