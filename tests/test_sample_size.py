"""testing sample size function"""
from app.config import Config
from app.PandasCalculations.calculations import MathSquare, SampleSize


def test_sample_size():
    """Checks to ensure that the correct sample size is returned"""
    population = 425
    z_score = 2.58
    margin_of_error = .05
    margin_of_error_squared = MathSquare.square(margin_of_error)
    z_score_squared = round(MathSquare.square(z_score), Config.rounding_precision)
    pop_std = .5

    assert SampleSize.get_sample_size(pop_std, z_score_squared
                                      , margin_of_error_squared, population) == 259.44

    population2 = 52
    z_score2 = 2.58
    margin_of_error2 = .05
    margin_of_error_squared2 = MathSquare.square(margin_of_error2)
    z_score_squared2 = round(MathSquare.square(z_score2), Config.rounding_precision)
    pop_std2 = .5

    assert SampleSize.get_sample_size(pop_std2, z_score_squared2,
                                      margin_of_error_squared2, population2) == 48.23
