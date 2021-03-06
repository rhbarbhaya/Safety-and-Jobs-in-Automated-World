"""
Project submission towards the ANLY 699 project
This project shows the flight information and getting some trend lines
https://transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FIL&QO_fu146_anzr=Nv4%20Pn44vr45
https://jblevins.org/notes/airline-data
"""
import os
import matplotlib.pyplot as plt
import pandas as pd


class Aviation:
    """
    class declaration for access control
    """
    def __init__(self) -> None:
        """default class, calling on the main function to avoid running double scripts
        There are no return types for this function.
        """
        self.main()

    @staticmethod
    def read_dataset(input_file_path) -> object:
        """Read the csv file from the given input filepath
        Returns pandas dataframe object
        """
        return pd.read_csv(input_file_path)

    @staticmethod
    def data_graph(data) -> None:
        """creates a scatter graph based on the group by parameter for time with
        count as the objective for this project
        """
        _data_ = data.groupby(
            by=['YEAR'],
            sort=True,
            as_index=True
        )['UNIQUE_CARRIER'].count().reset_index(name='Flights')
        print(_data_.to_string())
        plt.scatter(_data_['YEAR'], _data_['Flights'], label='Flights by year')
        plt.xlabel("Year")
        plt.ylabel("Flights")
        # plt.title("Count of Flights by Major Airline(s) in the USA by Year")
        plt.grid(visible=True, linestyle=':')
        plt.legend()
        plt.show()

    def main(self, data_directory='../data/aviation-flights') -> None:
        """Main function to read in all the files in scope and output a scatter plot
        :param data_directory: relative path from py file to the folder where files are located
        :type data_directory: str
        :return: None, outputs a groph for the paper
        :rtype: None
        """
        _data_ = pd.DataFrame()
        for file in os.listdir(data_directory):
            _data_ = pd.concat([self.read_dataset(os.path.join(data_directory, file)), _data_])
        print("File Read Complete")
        # _data_.to_csv("../output/aviation_flights/aviation_flights.csv")
        # print(_data_.describe().apply(lambda s: s.apply('{0:.5f}'.format)))
        # print(_data_.shape)
        self.data_graph(_data_)


aviation = Aviation()
