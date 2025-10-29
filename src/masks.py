from mypy.types import (Union)
import logging
import os

# Создание папки logs, если она не существует
if not os.path.exists('logs'):
    os.makedirs('logs')

# Настройка логирования для модуля masks
logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""
    logger.debug(f"Получение маски для номера карты: {card_number}")

    # Проверка, что номер карты составляет 16 цифр.
    if len(card_number) != 16 or not card_number.isdigit():
        logger.error("Ошибка: Номер карты должен содержать 16 цифр.")
        raise ValueError("Номер карты должен содержать 16 цифр.")

    card_number_new = card_number.replace(" ", "")
    mask_card_number = card_number_new[:4] + " " + card_number_new[4:6] + "** **** " + card_number_new[-4:]
    logger.info(f"Маска карты успешно создана: {mask_card_number}")

    return mask_card_number


def get_mask_account(number_account: Union[str]) -> str:
    """Функция маскировки банковского счёта"""
    logger.debug(f"Получение маски для номера счета: {number_account}")

    # Проверяем, что номер счета состоит как минимум из 4 цифр
    if len(number_account) != 20 or not number_account.isdigit():
        logger.error("Ошибка: Номер счета должен содержать 20 цифр.")
        raise ValueError("Номер счета должен содержать 20 цифр.")

    mask_account = "**" + number_account[-4:]
    logger.info(f"Маска счета успешно создана: {mask_account}")

    return mask_account


# if __name__ == "__main__":
#     print(get_mask_card_number("7000792289606361"))
#     print(get_mask_card_number("7000 7922 8960 6361"))
#     print(get_mask_card_number("7000792289606361"))
#     print(get_mask_account("73654108430135874305"))
