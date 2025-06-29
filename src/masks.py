from mypy.types import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""

    card_number_new = card_number.replace(" ", "")
    mask_card_number = card_number_new[:4] + " " + card_number_new[4:6] + "** **** " + card_number_new[-4:]
    return mask_card_number


def get_mask_account(number_account: Union[str]) -> str:
    """Функция маскировки банковского счёта"""
    mask_account = "**" + number_account[-4:]
    return mask_account


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_card_number("7000 7922 8960 6361"))
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
