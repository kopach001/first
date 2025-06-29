from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card: str) ->str:
    """Функция обработки информации о картах и счетах"""
    if "счет" in account_card.lower():
        card_number = account_card[-20:]
        mask_card = get_mask_account(card_number)
        return f'Счет {mask_card}'
    else:
        card_number = account_card[-16:]
        mask_card = get_mask_account(card_number)
        name_operator = account_card[:-16]
        return f'{name_operator} {mask_card}'

def get_date(format_date: str) -> str:
    """Функция изменения формата даты"""
    correct_date = format_date[8:11] + "." + format_date[5:7] + "." + format_date[:4]
    return correct_date

if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))