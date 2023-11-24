import pandas
import pandas as pd
from app.config import Config


class PandasReadCsv:
    """"Reads a path and returns a csv file"""

    @staticmethod
    def read_csv(absolute_path: str):
        return pd.read_csv(absolute_path)


class PandasMean:
    """Returns the mean of a database"""

    @staticmethod
    def mean_of_database(data_frame: pandas.DataFrame, field_name):
        return data_frame[field_name].mean()


class PandasMin:
    """Returns the min of a database"""

    @staticmethod
    def get_min_of_database(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].min()


class PandasMax:
    """Returns the max of a database"""

    @staticmethod
    def database_max(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].max()


class PandasMedian:
    """Returns the median of a database"""

    @staticmethod
    def median_of_database(data_frame: pandas.DataFrame, field_name):
        return data_frame[field_name].median()


class PandasVariance:
    """Returns the variance of a database"""

    @staticmethod
    def get_variance_of_database(data_frame: pandas.DataFrame, field_name):
        return data_frame[field_name].var()


class PandasPopulation:
    """Returns the population of a database"""

    @staticmethod
    def get_shape_of_database(data_frame: pandas.DataFrame, field_name):
        return data_frame[field_name].shape[0]


class PandasStd:
    """Returns the STD of a database"""

    @staticmethod
    def get_std_of_database(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].std()


class PandasMode:
    """Returns the mode of a database"""

    @staticmethod
    def get_mode_of_database(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].mode()


class RoundingToAppConfig:
    """Rounds numbers to certain # of decimal points"""

    @staticmethod
    def round_values(value):
        return round(value, Config.rounding_precision)


class MathSquare:
    """Returns the square of a number"""

    @staticmethod
    def square(value):
        return pow(value, 2)


class SampleSize:
    """Returns the sample size of a database"""

    @staticmethod
    def get_sample_size(pop_std, z_score_squared: int, margin_of_error_squared: int, population: int):
        return round((((z_score_squared * (pop_std * pop_std)) / margin_of_error_squared)
                      / (1 + (z_score_squared * pop_std * pop_std) / (margin_of_error_squared * population))), 2)
