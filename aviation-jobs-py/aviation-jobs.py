"""getting the dataset for the aviation jobs

Returns:
    None: plot for the dataset
"""
import pandas as pd
import matplotlib.pyplot as plt

class AviationJobs:
    """aviation jobs is the dataset from Bureau of Labor Statistics where aviation data is hosted
    Link: https://beta.bls.gov/dataViewer/view/timeseries/PCU481---481---
    This dataset contains all the scheduled aviation jobs from 1992 to 2022

    """
    def __init__(self) -> None:
        pass

    def read_dataset(self, filepath='../data/aviaton-jobs/file.csv') -> object:
        """Function for reading the dataset and returning the resulting pandas.DataFrame

        Args:
            filepath (str, optional): get the filepath to the file.
            Defaults to './data/aviaton-jobs/file.csv'.

        Returns:
            object: pandas.DataFrame object containing the whole dataset for aviation jobs
        """
        return pd.read_csv(filepath)

    def plot_data_by_group(self, _data_, groupby, summing_value, sort=True,
    as_index=False) -> None:
        """plotting the value -- jobs by year

        Args:
            _data_ (object): get the data from input
            groupby (list): get the groupby metric
            summing_value (str): get the column which contains the result
            sort (bool, optional): Should the data which is used to group be sorted?
            Defaults to True.
            as_index (bool, optional): Should the grouping value be the index?
            Defaults to False.
        """
        _data_ = _data_.groupby(by=groupby, sort=sort, as_index=as_index)[summing_value].sum()
        _data_ = _data_.drop(_data_.tail(1).index)
        plt.scatter(_data_['Year'], _data_['Value'], color='blue',
        label='Jobs in aviation industry')
        print(_data_.to_string())
        plt.xlabel("Year")
        plt.ylabel("Jobs")
        plt.grid(visible=True, linestyle=':')
        # plt.title("Jobs in aviation industry by year")
        plt.legend()
        plt.show()
        return None

    def results(self) -> None:
        """Main controller of the whole script
        """
        jobs_dataset = self.read_dataset()
        jobs_dataset.to_csv("../output/aviation_jobs/aviation_jobs.csv")
        self.plot_data_by_group(jobs_dataset, groupby=['Year'], summing_value='Value')

AviationJobs().results()
