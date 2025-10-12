import json
import os


def load_transactions(file_path):
    """Загрузить транзакции из JSON-файла."""
    if not os.path.isfile(file_path):
        return []  # Если файл не существует, вернуть пустой список

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):  # Проверка на список
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []