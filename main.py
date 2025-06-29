from src.masks import get_mask_account, get_mask_card_number

result = get_mask_card_number("7000792289606361")
print(result)

result = get_mask_account("73654108430135874305")
print(result)
