"""Test the pandas population function"""
import pandas as pd
from pandas import DataFrame
from app.PandasCalculations.calculations import PandasPopulation


def test_pandas_population():
    """test to check the count of the population"""

    data = [{'a': 1, 'b': 2, 'c': 3},
            {'a': 10, 'b': 20, 'c': 30}]

    data_frame: DataFrame = pd.DataFrame(data)

    assert PandasPopulation.get_shape_of_database(data_frame, 'a') == 2
