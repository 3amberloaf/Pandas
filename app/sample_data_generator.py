"""This is the main startup of the app"""
import os
import pandas
from app.PandasCalculations.calculations import RoundingToAppConfig, \
    PandasMean, PandasMedian, PandasMin, PandasMax, \
    PandasMode, PandasStd, MathSquare, SampleSize, PandasReadCsv, PandasVariance, PandasPopulation
from app.config import Config
from app.file_ops import FileOperations


def main():
    """This is the main function that is run"""


if __name__ == '__main__':
    """This causes the hello world function to be called if this is the __main__ top level of code"""
    main()
    # all for initial state_population
    absolute_path = str(FileOperations.get_calculate_file_path(Config.data_directory, Config.data_file_name))
    # Returning it as a dataframe
    initial_data_frame = PandasReadCsv.read_csv(absolute_path)
    initial_data_frame.columns = ["state", "pop"]

    print(initial_data_frame.to_string())

    # Return the mean of pop column
    pop_mean = PandasMean.mean_of_database(initial_data_frame, "pop")
    print(pop_mean)

    # Return the median of pop column
    pop_median = PandasMedian.median_of_database(initial_data_frame, "pop")
    print(pop_median)

    # Return the min of pop column
    pop_min = PandasMin.get_min_of_database(initial_data_frame, "pop")
    print(pop_min)

    # Return the max of pop column
    pop_max = PandasMax.database_max(initial_data_frame, "pop")
    print(pop_max)

    # Return the mode of pop column
    pop_mode = PandasMode.get_mode_of_database(initial_data_frame, "pop")
    print(pop_mode)

    # Return the variance of the pop column
    pop_variance = PandasVariance.get_variance_of_database(initial_data_frame, 'pop')
    print(pop_variance)

    # Return the std of the pop column, if over 1 then use .5
    pop_std = RoundingToAppConfig.round_values(PandasStd.get_std_of_database(initial_data_frame, "pop"))
    print(pop_std)
    used_std = .5

    # Find the total count of the pop column
    population = PandasPopulation.get_shape_of_database(initial_data_frame, "pop")
    print(population)
    # Find the sample size of the input

    z_score = 2.58
    margin_of_error = .05
    margin_of_error_squared = MathSquare.square(margin_of_error)
    z_score_squared = round(MathSquare.square(z_score), Config.rounding_precision)
    sample_size = SampleSize.get_sample_size(used_std, z_score_squared, margin_of_error_squared, population)
    sample_size = sample_size - int(4)
    print(sample_size)

    required_data = {'state': ['California', 'Wyoming'],
                     'pop': [39148760.0, 581836.0, 11641879.0, 4440204.0]}

    required_data_df = pandas.DataFrame(required_data)
    initial_data_frame.drop(initial_data_frame.index[initial_data_frame['state'] == "California"], inplace=True)
    initial_data_frame.drop(initial_data_frame.index[initial_data_frame['state'] == "Wyoming"], inplace=True)
    initial_data_frame.to_string()

    df_1 = initial_data_frame.sample(n=int(sample_size), replace=False, axis=None)
    df_1_final = pandas.concat([required_data_df, df_1], ignore_index=True)

    base_directory = os.path.dirname(os.path.abspath(__file__))
    sample_files_output_dir = os.path.join(base_directory, '', '../sample_files_output')
    df_1_final.to_csv(os.path.join(sample_files_output_dir, r'sample_data_number_2.58_0.05_48.csv'))
