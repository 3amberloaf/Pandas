# Introduction

This Python program leverages object-oriented programming (OOP) practices and the pandas library to analyze datasets. It efficiently selects a representative sample from a large dataset, and begins the process by choosing a specific column/field for analysis. Through various statistical measures such as min, max, median, mode, mean, standard deviation, and sample size, the program offers insightful characterization of the dataset.

# Object-Oriented Programming Techniques

This program focuses on advanced object-oriented programming (OOP) techniques to elevate code reusability and streamlining data manipulation. By structuring the code into classes and objects, it establishes a modular and organized architecture, as well as establishing a more scalable codebase. This approach enhances the clarity of the code as well as simplifies future modifications and additions. Therefore, making the program adaptable and robust.

## Classes and Objects

The program uses classes to represent entities like datasets, statistical measures, and test data files. Objects instantiated from these classes encapsulate data and behavior related to their respective entities. In the example below, the class `PandasMode` is created to return the mode of a database. Objects are instantiated from the `PandasMode` class.

```
class PandasMode:
    """Returns the mode of a database"""

    @staticmethod
    def get_mode_of_database(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].mode()
```

## Encapsulation

Encapsulation involves combining data and methods that operate on that data under a single unit (class). In this program, statistical measures, sample data, and test files could be encapsulated. As demonstrated in the previous code snippet, the class `PandasMode` encapsulates the function `get_mode_of_database` within the class itself. This practice of encapsulation allows for a clear separation of concerns and improves code organization.

```
class PandasMode:
    """Returns the mode of a database"""

    @staticmethod
    def get_mode_of_database(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].mode()
```

## Polymorphism

Polymorphism might be applied to allow different statistical measures to be applied to datasets using a common interface. In the following code snippet, polymorphism is expressed because each method is called on a different class, yet they all conform to the same interface for statistical analysis. This polymorphic behavior allows for a flexible and extensible design, where additional statistical measures can be added in the future without modifying the main code as long as they adhere to the shared interface. 

```
pop_mean = PandasMean.mean_of_database(initial_data_frame, "pop")
pop_median = PandasMedian.median_of_database(initial_data_frame, "pop")
pop_min = PandasMin.get_min_of_database(initial_data_frame, "pop")
pop_max = PandasMax.database_max(initial_data_frame, "pop")
pop_mode = PandasMode.get_mode_of_database(initial_data_frame, "pop")
pop_variance = PandasVariance.get_variance_of_database(initial_data_frame, 'pop')
pop_std = RoundingToAppConfig.round_values(PandasStd.get_std_of_database(initial_data_frame, "pop"))
```

## Abstraction

Abstraction involves simplifying complex systems by modeling classes based on their essential properties. To illustrate, the following code demonstrates abstraction by encapsulating the functionality of calculating the mode of a database within the `PandasMode` class. 

```
class PandasMode:
    """Returns the mode of a database"""

    @staticmethod
    def get_mode_of_database(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].mode()
```

# Programming Skills

This program demonstrated a variety of programming skills such as statistical analysis, algorithm design, file handling,  randomization, testing, and overall showcased an emphasis on clear and readable code.

## Statistical Analysis

The program demonstrates a solid understanding of statistical concepts by applying measures like min, max, median, mode, mean, and standard deviation to analyze datasets. The following is an example of the mode being found through the `PandasMode` class. 

```
class PandasMode:
    """Returns the mode of a database"""

    @staticmethod
    def get_mode_of_database(data_frame: pandas.DataFrame, field_name: str):
        return data_frame[field_name].mode()
```

## Algorithm Design

The algorithmic aspect of calculating sample size from a large dataset indicates proficiency in designing algorithms to solve specific problems.

```
class SampleSize:
    """Returns the sample size of a database"""

    @staticmethod
    def get_sample_size(pop_std, z_score_squared: int, margin_of_error_squared: int, population: int):
        return round((((z_score_squared * (pop_std * pop_std)) / margin_of_error_squared)
                      / (1 + (z_score_squared * pop_std * pop_std) / (margin_of_error_squared * population))), 2)
```

## File Handling

The program showcases skills in file handling, as it saves the resulting sample datasets to disk for future use.

```
    base_directory = os.path.dirname(os.path.abspath(__file__))
    sample_files_output_dir = os.path.join(base_directory, '', '../sample_files_output')
    df_1_final.to_csv(os.path.join(sample_files_output_dir, r'sample_data_number_2.58_0.05_48.csv'))
```

## Randomization

The random selection of records for sample data creation reflects programming skills related to randomization, ensuring that each record is unique. The following example uses `sample(n=sample_size)` to randomize the samples taken by the number of samples.

```
df_1 = initial_data_frame.sample(n=int(sample_size), replace=False, axis=None)
```

## Testing Strategy Implementation

Incorporating a detailed testing strategy is important to ensuring the reliability and success of any program. A number of test cases were designed to evaluate the functionality of critical components, ranging from statistical measures to the calculation of sample sizes. By employing testing methodologies such as unit testing, the program systematically validates individual units of code, ensuring that each class and function performs as intended. Below is one example of a function created to test that `PandasMax` is running successfully.

```
def test_pandas_max():
    """Test to see if the max is returned"""
    data = [{'a': 1, 'b': 2, 'c': 3},
            {'a': 10, 'b': 20, 'c': 30}]

    data_frame: DataFrame = pd.DataFrame(data)

    assert PandasMax.database_max(data_frame, 'a') == 10
```

## Code Organization and Readability

The organization of the program into sections such as calculations, data, tests, shows an emphasis on code readability and modular design.

# Program Overview

The program is composed of three main components; calculation classes, test functions, and the data. The following is a list of the topics covered and a general explaination.

## Sample Size Calculation

Sample size is crucial to ensuring that the selected subset is a fair representative of the entire population. The program employs a formula to calculate the correct sample size from the large dataset.

## Sample Data Creation

The program selects representative records for min and max values, with the remaining records  randomly chosen from the population dataset. This allows each record to be unique.
We create 15 test data files, each with different confidence intervals and margins of error.

## Testing Strategy

The generated sample datasets can be used at various stages of development to test different aspects of the program, such as memory usage.
As the program progresses, developers can increase the size of the input data for more comprehensive testing.

## File Saving

The resulting sample datasets are saved to disk for future use in development.

## Repeatability

The program ensures that each record in the sample dataset is unique, avoiding repetitions.

## Confidence Interval and Margin of Error

The program generates 15 test data files using specified values for confidence interval and margin of error, allowing for a diverse set of test scenarios.
