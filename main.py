from src.bank_search import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_transactions import read_csv_transactions, read_excel_transactions
from src.utils import financial_transaction
from src.widget import get_date, mask_account_card


def norm_input(text):
    """Приводим ввод пользователей к нижнему регистру"""
    return text.lower()


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Выбор источника данных
    while True:
        choice = input("Пользователь: ").strip()
        if choice == "1":
            print("Для обработки выбран JSON-файл.")
            path = "data/operations.json"
            transactions = financial_transaction(path)
            break
        elif choice == "2":
            print("Для обработки выбран CSV-файл.")
            path = "data/operations.csv"
            try:
                transactions = read_csv_transactions(path)
            except Exception as e:
                print(f"Ошибка при чтении CSV-файла: {e}")
                print("Файл не найден или повреждён. Используем JSON вместо CSV.")
                path = "data/operations.json"
                transactions = financial_transaction(path)
                break
        elif choice == "3":
            print("Для обработки выбран XLSX-файл.")
            path = "data/operations.xlsx"
            try:
                transactions = read_excel_transactions(path)
            except Exception as e:
                print(f"Ошибка при чтении XLSX-файла: {e}")
                print("Файл не найден или повреждён. Используем JSON вместо XLSX.")
                path = "data/operations.json"
                transactions = financial_transaction(path)
                break
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")

    valid_states = {"executed", "canceled", "pending"}
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_input = input("Пользователь: ").strip()
        normalized = norm_input(user_input)

        if normalized in valid_states:
            state_upper = normalized.upper()
            print(f'Операции отфильтрованы по статусу "{state_upper}"')
            transactions = filter_by_state(transactions, state_upper)
            break
        else:
            print(f'Статус операции "{user_input}" недоступен.')

    print("Отсортировать операции по дате? Да/Нет")
    sort_choice = norm_input(input("Пользователь: "))
    if sort_choice in ("да", "yes", "y"):
        print("Отсортировать по возрастанию или по убыванию?")
        order_choice = norm_input(input("Пользователь: "))
        reverse = "убыв" in order_choice
        transactions = sort_by_date(transactions, reverse=reverse)

    print("Выводить только рублевые транзакции? Да/Нет")
    rub_choice = norm_input(input("Пользователь: "))
    if rub_choice in ("да", "yes", "y"):
        transactions = list(filter_by_currency(transactions, "руб."))

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    desc_choice = norm_input(input("Пользователь: "))
    if desc_choice in ("да", "yes", "y"):
        keyword = input("Введите слово для фильтрации: ").strip()
        transactions = process_bank_search(transactions, keyword)

    print("Распечатываю итоговый список транзакций...")
    print()

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        print()
        for transaction in transactions:
            date_str = transaction.get("date", "")
            formatted_date = get_date(date_str)
            description = transaction.get("description", "")
            from_ = transaction.get("from", "")
            to = transaction.get("to", "")
            amount = transaction["operationAmount"]["amount"]
            currency = transaction["operationAmount"]["currency"]["name"]

            print(f"{formatted_date} {description}")
            if from_:
                masked_from = mask_account_card(from_)
                masked_to = mask_account_card(to)
                print(f"{masked_from} -> {masked_to}")
            else:
                masked_to = mask_account_card(to)
                print(masked_to)
            print(f"Сумма: {amount} {currency}")
            print()


if __name__ == "__main__":
    main()
