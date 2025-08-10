from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(inform_account_card: str) -> str:
    """Функция обрабатывает информацию о картах и о счетах"""
    if "счет" in inform_account_card.lower():
        number_card = inform_account_card[-20:]
        mask_card = get_mask_account(number_card)
        return f"Счет {mask_card}"
    else:
        number_card = inform_account_card[-16:]
        mask_card = get_mask_card_number(number_card)
        name_bank = inform_account_card[:-16]
        return f"{name_bank}{mask_card}"


def get_date(formatting_date: str) -> str:
    """Функция меняет формат даты"""
    correct_data = formatting_date[8:10] + "." + formatting_date[5:7] + "." + formatting_date[:4]
    return correct_data


# if __name__ == "__main__":
#     print(mask_account_card("Visa Platinum 7000792289606361"))
#     print(mask_account_card("Maestro 7000792289606361"))
#     print(mask_account_card("Счет 73654108430135874305"))
#     print(get_date("2024-03-11T02:26:18.671407"))
