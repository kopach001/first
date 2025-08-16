from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from data.transaction_data import transactions


def test_filter_by_currency_correct_filtering() -> None:
    # Проверяем, что фильтр возвращает только транзакции с валютой USD
    result = filter_by_currency(transactions, "USD")
    # Все возвращённые транзакции должны иметь currency code 'USD'
    assert all(i["operationAmount"]["currency"]["code"] == "USD" for i in result)
    # И при этом в исходных данных есть такие транзакции
    assert any(i["operationAmount"]["currency"]["code"] == "USD" for i in transactions)


def test_filter_by_currency_no_matches() -> None:
    result = list(filter_by_currency(transactions, ['USD', 'RUB']))
    assert result == []  # должно вернуть пустой список


def test_filter_by_currency_empty_list() -> None:
    empty_list: list = []
    result = list(filter_by_currency(empty_list, "USD"))
    assert result == []


def test_filter_by_currency_no_matching_transactions() -> None:
    # Создаём список без нужной валюты
    no_usd_transactions = [
        {"id": 1, "operationAmount": {"amount": "100", "currency": {"name": "EUR", "code": "EUR"}}},
        {"id": 2, "operationAmount": {"amount": "200", "currency": {"name": "JPY", "code": "JPY"}}},
    ]
    assert not list(filter_by_currency(no_usd_transactions, "USD"))