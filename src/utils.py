import json
import logging
from pathlib import Path

log_file = Path(__file__).parent.parent / "logs" / "utils.log"

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def financial_transaction(path_to_file):
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path_to_file: путь до .json-файла
    :return: список словарей с данными о финансовых транзакциях
    """
    file_path = Path(path_to_file)
    try:
        if not file_path.exists():
            logger.warning("вернулся пустой список, так как отсутствует файл")
            return []
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info("вернулся список словарей с данными о финансовых транзакциях")
                return data
            else:
                logger.warning("вернулся пустой список, так как файл пустой")
                return []
    except (json.JSONDecodeError, PermissionError):
        logger.warning("некорректный формат файла")
        return []
