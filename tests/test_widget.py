import pytest

from src.widget import get_date, mask_account_card

test_mask_account_card = [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Счет 646864736788947795891", "Счет **5891"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет abc1", "номер счета должен состоять только из цифр"),
    ("Maestro 1А96Б3Е8T87Y5W9X", "номер карты должен состоять только из цифр"),
    ("Счет ", "номер счета должен состоять только из цифр"),
    ("Maestro ", "номер карты должен состоять только из цифр"),
]

test_get_date = [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024-03-11T02:26:18.671", "Некорректное значение"),
    ("", "Отсутствует дата"),
    ("2124-13-32T02:26:18.671407", "Некорректная дата"),
]


@pytest.mark.parametrize("card_details, expected_result", test_mask_account_card)
def test_mask_account_card(card_details, expected_result):
    assert mask_account_card(card_details) == expected_result


@pytest.mark.parametrize("unformatted_date, expected_result", test_get_date)
def test_get_date(unformatted_date, expected_result):
    assert get_date(unformatted_date) == expected_result
