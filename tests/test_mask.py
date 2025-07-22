import pytest

from src.masks import get_mask_account, get_mask_card_number

test_card = [
    ("7000792289606361", "7000 79** **** 6361"),
    ("abc1", "номер карты должен состоять только из цифр"),
    ("70007922896063611", "Не соответствующая длина карты (16 цифр)"),
    ("", "Не соответствующая длина карты (16 цифр)"),
    ("123456789012345", "Не соответствующая длина карты (16 цифр)"),
]

test_account = [
    ("73654108430135874305", "**4305"),
    ("abc1", "номер счета должен состоять только из цифр"),
    ("70007922896063611", "Не соответствующая длина счета (20 цифр)"),
    ("", "Не соответствующая длина счета (20 цифр)"),
    ("123456789012345", "Не соответствующая длина счета (20 цифр)"),
]


@pytest.mark.parametrize("card_number, expected_result", test_card)
def test_get_mask_card_number(card_number, expected_result):
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize("account_number, expected_result", test_account)
def test_get_mask_account(account_number, expected_result):
    assert get_mask_account(account_number) == expected_result
