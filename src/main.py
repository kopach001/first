from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date

result = get_mask_card_number("7000792289606361")
print(result)

result = get_mask_account("73654108430135874305")
print(result)

result = get_date("2024-03-11T02:26:18.671407")
print(result)
