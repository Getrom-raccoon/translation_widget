import pytest
from src.bank_operations import process_bank_operations


@pytest.fixture
def sample_transactions():
    return [
        {"description": "Оплата ЖКХ за август", "amount": 5000},
        {"description": "Покупка в магазине Пятёрочка", "amount": 1200},
        {"description": "Перевод на карту другу", "amount": 3000},
        {"description": "Оплата мобильной связи", "amount": 800},
        {"description": "Покупка продуктов в Магните", "amount": 950},
        {"description": "Возврат за товар", "amount": -1500},
        {"description": "Оплата интернета", "amount": 600},
        {"description": "Заправка автомобиля", "amount": 2500},
        {"description": "Покупка в Спортмастере", "amount": 4200},
        {"description": "Подписка на онлайн-кинотеатр", "amount": 599},
    ]


def test_basic_category_counting(sample_transactions):
    categories = ["Оплата", "Покупка", "Перевод", "Подписка"]
    result = process_bank_operations(sample_transactions, categories)

    assert result == {"Оплата": 3, "Покупка": 3, "Перевод": 1, "Подписка": 1}


def test_word_boundary_matching(sample_transactions):
    categories = ["Оплата", "Покупка", "нет"]
    result = process_bank_operations(sample_transactions, categories)

    assert result["Оплата"] == 3
    assert result["Покупка"] == 3
    assert result["нет"] == 0


def test_category_not_found(sample_transactions):
    categories = ["Аренда", "Ипотека", "Кредит"]
    result = process_bank_operations(sample_transactions, categories)

    assert result == {"Аренда": 0, "Ипотека": 0, "Кредит": 0}


def test_empty_transaction_list():
    categories = ["Оплата", "Покупка"]
    result = process_bank_operations([], categories)
    assert result == {"Оплата": 0, "Покупка": 0}


def test_empty_categories_list(sample_transactions):
    result = process_bank_operations(sample_transactions, [])
    assert result == {}


def test_partial_word_not_matched():
    data = [
        {"description": "Оплатил такси"},
        {"description": "Доплата за обучение"},
        {"description": "Оплата за квартиру"},
    ]
    categories = ["Оплата"]
    result = process_bank_operations(data, categories)
    assert result["Оплата"] == 1


def test_subword_not_counted():
    data = [
        {"description": "Переплата по кредиту"},
        {"description": "Оплата по счету"},
        {"description": "Автоплатеж активирован"},
    ]
    categories = ["плата"]
    result = process_bank_operations(data, categories)

    assert result["плата"] == 0


def test_duplicate_categories():
    data = [{"description": "Оплата интернета"}]
    categories = ["Оплата", "Оплата", "Покупка"]
    result = process_bank_operations(data, categories)

    assert "Оплата" in result
    assert result["Оплата"] == 2
    assert result["Покупка"] == 0
    assert len(result) == 2
