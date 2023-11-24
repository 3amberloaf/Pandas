"""Test function to check that Pandas STD works"""

import pandas as pd
from pandas import DataFrame
from app.PandasCalculations.calculations import PandasStd


def test_pandas_std():
    """Check to see that the STD is returned"""
    data = [{'a': 1, 'b': 2, 'c': 3},
            {'a': 10, 'b': 20, 'c': 30}]

    data_frame: DataFrame = pd.DataFrame(data)

    assert PandasStd.get_std_of_database(data_frame, 'a') == 6.363961030678928
