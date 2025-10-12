import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "inform_card, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_card(inform_card: str, expected: str) -> None:
    assert mask_account_card(inform_card) == expected


@pytest.mark.parametrize(
    "inform_account, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account(inform_account: str, expected: str) -> None:
    assert mask_account_card(inform_account) == expected


@pytest.mark.parametrize(
    "formatting_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-09-21T02:26:18.671407", "21.09.2024"),
        ("2024-01-01T02:26:18.671407", "01.01.2024"),
        ("2023-10-16T02:26:18.671407", "16.10.2023"),
    ],
)
def test_get_date(formatting_date: str, expected: str) -> None:
    assert get_date(formatting_date) == expected
