from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(card_details: str) -> str:
    """функция обрабатывает информацию как о картах, так и о счетах"""
    mask_account = get_mask_account(card_details[-20:])
    mask_card = get_mask_card_number(card_details[-16:])

    if card_details[0:4] == "Счет":
        return card_details[0:5] + mask_account
    else:
        return card_details[:-16] + mask_card


def get_date(unformatted_date: str) -> str:
    """возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    formatted_date = unformatted_date[8:10] + unformatted_date[4:8] + unformatted_date[0:4]
    return formatted_date.replace("-", ".")