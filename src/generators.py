from typing import Generator


def filter_by_currency(transactions, currency):
    """Фильтрует транзакции по коду валюты"""
    filter_transaction = filter(
        lambda x: x.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency, transactions
    )
    for item in filter_transaction:
        yield item


def transaction_descriptions(transactions):
    """Возвращает описание транзакции"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str]:
    """Генератор, выдает номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        format_number = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
        yield format_number
