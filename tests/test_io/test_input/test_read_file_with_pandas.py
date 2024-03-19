from app.io.input import read_file_with_pandas
import pytest
import pandas as pd
"""
Module for testing the read_file_with_pandas() function in the app.io.input module.
For testing, pytest is used.
"""

RESOURCES = './tests/data/'


def test_FileNotFoundError():
    with pytest.raises(FileNotFoundError):
        read_file_with_pandas('csv.csv')

def test_read_csv():
    path = "../../data/csv.csv"
    df_expected = pd.DataFrame({
        'ter': ['try', None],
        'two': ['one', 'text'],
        'three': ['four', None]
    })

    df_expected.to_csv(path, index=False)
    df_result = read_file_with_pandas(path)

    pd.testing.assert_frame_equal(df_expected, df_result)

def test_read_json():
    path = "../../data/json.json"
    df_expected = pd.DataFrame({
        'ter': ['try', None],
        'two': ['one', 'text'],
        'three': ['four', None]
    })

    df_expected.to_json(path)
    df_result = read_file_with_pandas(path)

    pd.testing.assert_frame_equal(df_expected, df_result)
