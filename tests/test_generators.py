from data.transaction_data import transactions
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_correct_filtering() -> None:
    # Проверяем, что фильтр возвращает только транзакции с валютой USD
    result = filter_by_currency(transactions, "USD")
    # Все возвращённые транзакции должны иметь currency code 'USD'
    assert all(i["operationAmount"]["currency"]["code"] == "USD" for i in result)
    # И при этом в исходных данных есть такие транзакции
    assert any(i["operationAmount"]["currency"]["code"] == "USD" for i in transactions)


def test_filter_by_currency_no_matches() -> None:
    result = list(filter_by_currency(transactions, ["USD", "RUB"]))
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


def test_transaction_descriptions_correct() -> None:
    """Проверяем, возвращённый список совпадает с полями description исходных данных"""
    descriptions = list(transaction_descriptions(transactions))
    expected_descriptions = [i["description"] for i in transactions]
    assert descriptions == expected_descriptions


def test_transaction_descriptions_empty() -> None:
    """Пустой список == пустой список"""
    result = list(transaction_descriptions([]))
    assert result == []


def test_transaction_descriptions_multi() -> None:
    several_transactions = [{"description": "Перевод"}, {"description": "Покупка"}, {"description": "Оплата услуги"}]
    result = list(transaction_descriptions(several_transactions))
    assert result == ["Перевод", "Покупка", "Оплата услуги"]


def test_card_number_generator_range() -> None:
    start = 1
    end = 3
    gen = card_number_generator(start, end)
    results = list(gen)

    assert len(results) == (end - start + 1)

    for i, number in enumerate(results, start=start):
        expected = f"{i:016d}"
        expected_format = " ".join(expected[y : y + 4] for y in range(0, 16, 4))
        assert number == expected_format


def test_card_number_format() -> None:
    start = 1234567890123456
    end = 1234567890123456
    gen = card_number_generator(start, end)
    result = next(gen)

    # Проверяем форматирование: должно быть 4 группы по 4 цифры
    parts = result.split(" ")
    assert len(parts) == 4
    for part in parts:
        assert len(part) == 4
        assert part.isdigit()


def test_card_number_edge_cases() -> None:
    # Тест с диапазоном из одного числа.
    start_end = 7777777777777777
    gen = card_number_generator(start_end, start_end)
    result = next(gen)

    expected_str = f"{start_end:016d}"
    expected_format = " ".join([expected_str[y : y + 4] for y in range(0, 16, 4)])

    assert result == expected_format


def test_card_number_generation_completes() -> None:
    # Проверка, что генератор завершает работу после последнего числа
    start = 10
    end = 12
    gen = card_number_generator(start, end)

    results = list(gen)

    # Количество должно быть равным диапазону +1
    assert len(results) == (end - start + 1)

    # Проверяем последовательность номеров
    for i, number in enumerate(results, start=start):
        expected_str = f"{i:016d}"
        expected_formatted = " ".join([expected_str[y : y + 4] for y in range(0, 16, 4)])
        assert number == expected_formatted
