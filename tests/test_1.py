def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    #print(card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[-4:])
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(get_mask_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    #print("**" + get_mask_account[-4:])
    return f"**{get_mask_account[-4:]}"


print(get_mask_card_number("7000792289606361"))  # проверка работы первой функции
print(get_mask_account("73654108430135874305"))  # проверка работы второй функции
