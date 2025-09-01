from unittest.mock import Mock, patch
import pytest
from src.read_transactions import read_csv_transactions, read_excel_transactions


@patch("pandas.read_csv")
def test_read_csv_transactions(mock_read_csv):
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("fake_path.csv")

    mock_read_csv.assert_called_once_with("fake_path.csv")
    assert result == [{"id": 1, "amount": 100}]


@patch("pandas.read_excel")
def test_read_excel_transactions(mock_read_excel):
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": 200}]
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("fake_path.xlsx")

    mock_read_excel.assert_called_once_with("fake_path.xlsx")
    assert result == [{"id": 2, "amount": 200}]