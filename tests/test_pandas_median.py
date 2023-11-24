"""Test function to check that Pandas Median works"""

import pandas as pd
from pandas import DataFrame
from app.PandasCalculations.calculations import PandasMedian


def test_pandas_median():
    """Test to check that the median is returned"""
    data = [{'a': 1, 'b': 2, 'c': 3},
            {'a': 10, 'b': 20, 'c': 30}]

    data_frame: DataFrame = pd.DataFrame(data)

    assert PandasMedian.median_of_database(data_frame, 'a') == 5.5
