from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_details: str) -> str:
    """функция обрабатывает информацию как о картах, так и о счетах"""
    mask_account = get_mask_account(card_details[-20:])
    mask_card = get_mask_card_number(card_details[-16:])

    if card_details[0:4] == "Счет":
        if any(i.isalpha() for i in mask_account):
            return f"номер счета должен состоять только из цифр"
        else:
            return f"{card_details[0:5]}{mask_account}"
    elif any(i.isdigit() for i in mask_card):
        return f"{card_details[:-16]}{mask_card}"
    else:
        return f"номер карты должен состоять только из цифр"


def get_date(unformatted_date: str) -> str:
    """возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    formatted_date = str((f"{unformatted_date[8:10]}{unformatted_date[4:8]}{unformatted_date[0:4]}"
                .replace("-", ".")))

    if unformatted_date == "":
        return f"Отсутствует дата"
    elif len(unformatted_date) != 26:
        return f"Некорректное значение"
    elif (int(formatted_date[0:2]) > 12 or int(formatted_date[3:5]) > 31
          or int(formatted_date[6:]) > 2100):
        return f"Некорректная дата"
    else:
        return formatted_date
