from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[Any, Any]]:
    """Функция, которая фильтрует список словарей по указанному ключу"""
    sorted_list = []
    for key_state in data:
        if key_state.get("state", "") == state:
            sorted_list.append(key_state)
    return sorted_list


# Пример использования:
sample_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

filtered_executed = filter_by_state(sample_data)
print(filtered_executed)

filtered_canceled = filter_by_state(sample_data, "CANCELED")
print(filtered_canceled)


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует список операций по ключу 'date'"""
    # Преобразуем дату к объекту datetime, чтобы корректно отсортировать
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)


sorted_data_desc = sort_by_date(sample_data)
print(sorted_data_desc)
