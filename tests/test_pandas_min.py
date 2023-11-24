"""Test function to check that Pandas Min works"""

import pandas as pd
from pandas import DataFrame
from app.PandasCalculations.calculations import PandasMin


def test_pandas_min():
    """Test to check that the min is returned"""
    data = [{'a': 1, 'b': 2, 'c': 3},
            {'a': 10, 'b': 20, 'c': 30}]

    data_frame: DataFrame = pd.DataFrame(data)

    assert PandasMin.get_min_of_database(data_frame, 'a') == 1
