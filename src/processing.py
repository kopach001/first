from typing import Any


def filter_by_state(data: list[dict[str, Any]], user_state: str) -> list[dict[Any, Any]]:
    """Функция, которая фильтрует список словарей по указанному ключу"""
    sorted_list = []
    x for x in data if x.get("state", '') == user_state:
        sorted_list.append(x)
    return sorted_list


def sort_by_date(data: list[dict[str, Any]], descending: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки списка банковских операций по дате (по умолчанию - убывание)"""
    sorted_list = sorted(data, key=lambda x: x["date"], reverse=descending)
    return sorted_list