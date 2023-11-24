"""Test function to check that Pandas Max works"""
import pandas as pd
from pandas import DataFrame
from app.PandasCalculations.calculations import PandasMax


def test_pandas_max():
    """Test to see if the max is returned"""
    data = [{'a': 1, 'b': 2, 'c': 3},
            {'a': 10, 'b': 20, 'c': 30}]

    data_frame: DataFrame = pd.DataFrame(data)

    assert PandasMax.database_max(data_frame, 'a') == 10
