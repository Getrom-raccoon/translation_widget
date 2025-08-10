import logging
from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования начала, успешного завершения и ошибок выполнения функции
    :param filename:  Имя айла для записи лога. если имя не указано, запись идёт в консоль
    :return: Декоратор который оборачивает функцию и добавляет логирование
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            Обёртка - добавляющая логирование для функции
            :param args: позиционные аргументы подаются в оригинальную функцию
            :param kwargs: именованные аргументы подаются в оригинальную функцию
            :return: результат выполнения оригинальной функции
            """
            func_name = func.__name__

            start_message = f"{func_name} started"

            if filename:
                logging.getLogger().handlers.clear()
                logging.basicConfig(
                    filename=filename,
                    level=logging.INFO,
                    format="%(message)s",
                    encoding="utf-8"
                )
                logger = logging.getLogger()
                logger.info(start_message)
            else:
                print(start_message)
            try:
                result = func(*args, **kwargs)
                success_message = f"{func_name} ок"

                if filename:
                    logger.info(success_message)
                else:
                    print(success_message)

                return result
            except Exception as e:
                error_message = (
                    f"{func_name} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )

                if filename:
                    logger.error(error_message)
                    for h in logger.handlers:
                        h.close()
                        logger.removeHandler(h)
                else:
                    print(error_message)

                raise

        return wrapper

    return decorator

@log(filename="mylog.txt")
def my_function(x, y):
    """Складывает два числа"""
    return x + y

my_function(1, 0)