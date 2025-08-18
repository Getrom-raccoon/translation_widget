import json

def financial_transaction(path_to_file):
    try:
        with open(f'../{path_to_file}', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError or json.JSONDecodeError:
        return {}
print(financial_transaction('data/operations.json'))