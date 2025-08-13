from typing import Union

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("5555666677778888", "5555 66** **** 8888"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
    ],
)
def test_get_mask_card_number_ok(card_number: Union[str], expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("98765432198765432198", "**2198"),
        ("1234", "**1234"),
        ("23", "**23"),
        ("", "**"),
    ],
)
def test_get_mask_account(account_number: Union[str], expected: str) -> None:
    assert get_mask_account(account_number) == expected
