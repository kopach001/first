from unittest.mock import MagicMock, patch

import pytest

from src.data_reader import read_transactions_from_csv, read_transactions_from_excel



def test_():
    """Тестирование чтения траread_transactions_from_csvнзакций из CSV файла."""
    mock_data = MagicMock()
    mock_data.to_dict.return_value = [{"amount": 100, "currency": "USD"}]

    with patch("pandas.read_csv", return_value=mock_data), patch(
        "os.path.exists", return_value=True
    ):  # Подмена os.path.exists
        result = read_transactions_from_csv("mock_path.csv")
        assert result == [{"amount": 100, "currency": "USD"}]


def test_read_transactions_from_excel():
    """Тестирование чтения транзакций из Excel файла."""
    mock_data = MagicMock()
    mock_data.to_dict.return_value = [{"amount": 200, "currency": "EUR"}]

    with patch("pandas.read_excel", return_value=mock_data), patch(
        "os.path.exists", return_value=True
    ):  # Подмена os.path.exists
        result = read_transactions_from_excel("mock_path.xlsx")
        assert result == [{"amount": 200, "currency": "EUR"}]


def test_file_not_found_csv():
    """Тестирование обработки ошибки при отсутствии файла CSV."""
    with patch("os.path.exists", return_value=False):  # Подмена os.path.exists
        with pytest.raises(FileNotFoundError):
            read_transactions_from_csv("non_existent_file.csv")


def test_file_not_found_excel():
    """Тестирование обработки ошибки при отсутствии файла Excel."""
    with patch("os.path.exists", return_value=False):  # Подмена os.path.exists
        with pytest.raises(FileNotFoundError):
            read_transactions_from_excel("non_existent_file.xlsx")