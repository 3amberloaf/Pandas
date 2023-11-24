"""Test function to check that Pandas Mode works"""

import pandas as pd
from pandas import DataFrame
from app.PandasCalculations.calculations import PandasMode


def test_pandas_mode():
    """Test to check that the mode is returned"""
    data = [{'a': 1, 'b': 2, 'c': 3},
            {'a': 10, 'b': 20, 'c': 30},
            {'a': 10, 'b': 20, 'c': 30}]

    data_frame: DataFrame = pd.DataFrame(data)

    assert PandasMode.get_mode_of_database(data_frame, 'a').mode()[0] == 10
