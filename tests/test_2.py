from src.masks import get_mask_account, get_mask_card_number

#mask_account = get_mask_account((card_details[-1:-20]))
#get_mask_card = get_mask_card_number(card_number)

def mask_account_card(card_details):
    """функция обрабатывает информацию как о картах, так и о счетах."""
    mask_account = get_mask_account(card_details[-20:])
    mask_card = get_mask_card_number(card_details[-16:])
    #account_number = card_details[-20:]

    if card_details[0:4] == "Счет":
        return card_details[0:5] + mask_account
    else:
        return card_details[:-16] + mask_card



print(mask_account_card("Visa Platinum 8990922113665229"))



def get_date(unformatted_date: str) -> str:
    formatted_date = unformatted_date[8:10] + unformatted_date[4:8] + unformatted_date[0:4]
    #formatted_date = ".".join(unformatted_date[8:10], unformatted_date[5:7], unformatted_date[0:4])
    #formatted_date = unformatted_date[0:10]
    return formatted_date.replace("-",".")


print(get_date("2024-03-11T02:26:18.671407"))