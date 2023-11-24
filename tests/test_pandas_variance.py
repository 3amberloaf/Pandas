"""Test function to check that Pandas Variance works"""

import pandas as pd
from pandas import DataFrame
from app.PandasCalculations.calculations import PandasVariance


def test_pandas_variance():
    """Check to test that the variance is returned"""
    data = [{'a': 1, 'b': 2, 'c': 3},
            {'a': 10, 'b': 20, 'c': 30}]

    data_frame: DataFrame = pd.DataFrame(data)

    assert PandasVariance.get_variance_of_database(data_frame, 'a') == 40.5
