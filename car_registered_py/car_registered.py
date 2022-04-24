"""
This script is to get the car sales by year in the USA
https://www.bts.gov/content/annual-us-motor-vehicle-production-and-factory-wholesale-sales-thousands-units
"""
import pandas as pd
import matplotlib.pyplot as plt

class CarRegistered:
    """
    Get the cars registered in the USA and plot the totals by year
    """
    def __init__(self, input_file_path) -> None:
        """
        Auto-initialize the main function
        :param input_file_path: get the dataset file path
        :type input_file_path: str
        """
        self.main(input_file_path)

    @staticmethod
    def read_dataset(input_file_path) -> object:
        """
        read the dataset from the input file path and output the pandas dataframe object
        :param input_file_path: dataset file path in csv format
        :type input_file_path: str
        :return: pandas.DataFrame object of the input csv file path
        :rtype: object
        """
        return pd.read_csv(input_file_path, low_memory=False)

    @staticmethod
    def data_graph(_data_) -> None:
        """
        Generate a time series graph for the desired output with labels
        :param _data_: pandas dataframe object for the input file path that \
            has to be converted into a graph
        :type _data_: object
        :return: Plots a graph, doesn't have a return type
        :rtype: None
        """
        plt.figure(figsize=(12, 4))
        plt.scatter(_data_['Year'], _data_['Domestic sales, totalb'], label='Car sales by year')
        plt.xlabel("Year")
        plt.ylabel("Car Sales in thousands")
        plt.title("Car Sales in the USA by Year")
        plt.tick_params(axis='x', rotation=90)
        plt.legend()
        plt.show()

    def main(self, input_file_path) -> None:
        """
        Control center of the class function
        :param input_file_path: file path of the csv that is the dataset of this analysis
        :type input_file_path: str
        :return: None
        :rtype: None
        """
        data = self.read_dataset(input_file_path)
        self.data_graph(data)


CarRegistered('../data/car_registered/table_01_15_072021.csv')
