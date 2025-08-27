import logging
from pathlib import Path

log_file = Path(__file__).parent.parent / "logs" / "masks.log"

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    # Проверяем, содержит ли строка хотя бы одну букву
    if any(i.isalpha() for i in card_number):
        logger.error("номер карты должен состоять только из цифр")
        return "номер карты должен состоять только из цифр"

    # Проверяем длину строки
    if len(card_number) != 16:
        logger.error("Не соответствующая длина карты (16 цифр)")
        return "Не соответствующая длина карты (16 цифр)"

    # Если все проверки пройдены, возвращаем маску
    logger.info("все проверки пройдены, возвращаем маску")
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    # Проверяем, содержит ли строка хотя бы одну букву
    if any(i.isalpha() for i in account_number):
        logger.error("номер счета должен состоять только из цифр")
        return "номер счета должен состоять только из цифр"

    # Проверяем длину строки
    if len(account_number) != 20:
        logger.error("Не соответствующая длина счета (20 цифр)")
        return "Не соответствующая длина счета (20 цифр)"

    # Если все проверки пройдены, возвращаем маску
    logger.info("все проверки пройдены, возвращаем маску")
    return f"**{account_number[-4:]}"
