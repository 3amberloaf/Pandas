"""Test function to check that Pandas Mean works"""
import pandas as pd
from pandas import DataFrame
from app.PandasCalculations.calculations import PandasMean


def test_pandas_mean():
    """Test to check that the function returns the mean"""
    data = [{'a': 1, 'b': 2, 'c': 3},
            {'a': 10, 'b': 20, 'c': 30}]

    data_frame: DataFrame = pd.DataFrame(data)

    assert PandasMean.mean_of_database(data_frame, 'a') == 5.5
