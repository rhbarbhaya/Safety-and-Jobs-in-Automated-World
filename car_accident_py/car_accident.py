"""This module is for the cars involved in accidents dataset
https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/
https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars
"""
import os
import pandas as pd
import matplotlib.pyplot as plt


class CarAccident:
    """Car Accient is a class for getting the plot for fatalities in the USA.
    The data ranges 1975 to 2020
    """
    def __init__(self):
        """Default run and initial run for the project.
        """
        self.main()

    @staticmethod
    def read_files(directory: str, files: list) -> object:
        """Reading files from the data store, capturing all the accidents from 1975 to 2020
        :param directory: directory where files are stored
        :type directory: str
        :param files: list of all the files in the folder
        :type files: list
        :return: dataset with the scope of the data
        :rtype: object
        """
        for file in files:
            if 'accident' in file.lower():
                accident = pd.read_csv(os.path.join(directory, file), low_memory=False)
                accident['ST_CASE'] = accident['ST_CASE'].astype(str)
                accident['YEAR'] = ''.join(
                    filter(
                        lambda i:
                        i.isdigit(),
                        os.path.basename(directory)
                    )
                )
                accident = accident[['ST_CASE', 'MONTH', 'YEAR', 'FATALS']]
                return accident
        return None

    @staticmethod
    def data_graph(_data_) -> None:
        """Plotting the dataset to a timeseries graph by the year
        :param data: dataset scoped for plotting
        :type data: object
        :return: plots the dataset to a timeline
        :rtype: None
        """
        print(_data_.head())
        _data_ = _data_.groupby(
            by=[
                'YEAR'
            ],
            sort=True,
            as_index=True
        )[
            'FATALS'
        ].sum().reset_index(
            name='FATALS'
        )
        plt.scatter(_data_['YEAR'], _data_['FATALS'], label='Car fatalities by year')
        plt.xlabel("Year")
        plt.ylabel("Car Fatalities")
        plt.title("Car fatalities in the USA by Year")
        plt.tick_params(axis='x', rotation=90)
        plt.legend()
        plt.show()

    def main(self):
        """Controlling the class for getting the files and the plots for the dataset
        :return: plots the timeseries graph
        :rtype: None
        """
        stack_data = pd.DataFrame()
        for directory, _, files in os.walk('../data/car-accident'):
            if '.DS_Store' in files:
                pass
            else:
                accident = self.read_files(directory, files)
                stack_data = pd.concat([stack_data, accident])
        self.data_graph(stack_data)

CarAccident()
