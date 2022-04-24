"""
Script for plotting tesla's car and autopilot deaths
"""
import pandas as pd
pd.options.mode.chained_assignment = None
import matplotlib.pyplot as plt

class TeslaDeaths:
    """
    class for tesla deaths
    """
    def __init__(
            self,
            input_file_path: str
    ) -> None:
        """
        initiatizing main function as the default function
        :param input_file_path: input file path for the dataset
        :type input_file_path: str
        """
        self.main(
            input_file_path
        )

    @staticmethod
    def read_dataset(
            input_file_path: str
    ) -> object:
        """
        to read the dataset. Only csv
        :param input_file_path: input csv file path of the dataset
        :type input_file_path: str
        :return: pandas.DataFrame object of the csv file
        :rtype: object
        """
        return pd.read_csv(
            input_file_path,
            low_memory=False
        )

    @staticmethod
    def data_scope(
            data: object
    ) -> object:
        """
        Clean the file and correct the data types
        :param data: pandas.DataFrame object of the file
        :type data: object
        :return: scoped pandas dataframe
        :rtype: object
        """
        data: object = data[
            data[
                ' Country '
            ] == ' USA '
        ]
        data['Year']: object = data[
            'Year'
        ].astype(
            int
        )
        data: object = data[
            [
                'Year',
                ' Deaths ',
                ' AutoPilot claimed '
            ]
        ]
        data[' AutoPilot claimed ']: object = data[
            [
                ' AutoPilot claimed '
            ]
        ].replace(
            [' - '],
            [0]
        )
        data[' AutoPilot claimed ']: object = data[
            ' AutoPilot claimed '
        ].astype(
            int
        )
        data[' Deaths ']: object = data[
            ' Deaths '
        ].astype(
            int
        )
        return data

    @staticmethod
    def plot_by_year(
            data
    ) -> None:
        """
        Plot the deaths by year for both tesla related deaths and autopilot deaths
        :param data: pandas data frame object
        :type data: object
        :return: plot the graph
        :rtype: None
        """
        data: object = data[
            [
                'Year',
                ' Deaths ',
                ' AutoPilot claimed '
            ]
        ]
        data: object = data.groupby(
            by=[
                'Year'
            ],
            sort=True,
            as_index=False
        ).sum()
        fig, ax1 = plt.subplots()
        ax1.set_xlabel(
            'Year'
        )
        ax1.set_ylabel(
            'Deaths'
        )
        ax1.plot(
            data[
                'Year'
            ],
            data[
                ' Deaths '
            ],
            color='blue',
            label='Deaths involving Tesla'
        )
        ax1.tick_params(
            axis='y',
            labelcolor='blue'
        )

        ax2 = ax1.twinx()
        ax2.set_ylabel(
            'Autopilot Deaths'
        )
        ax2.plot(
            data[
                'Year'
            ],
            data[
                ' AutoPilot claimed '
            ],
            color='red',
            label='Autopilot deaths'
        )
        ax2.tick_params(
            axis='y',
            labelcolor='red'
        )
        fig.legend()
        plt.show()

    def main(
            self,
            input_file_path: str
    ) -> None:
        """
        Main function to control the script
        :param input_file_path: input file path of the csv file
        :type input_file_path: str
        :return: None
        :rtype: None
        """
        data: object = self.read_dataset(
            input_file_path
        )
        data: object = self.data_scope(
            data
        )
        self.plot_by_year(
            data
        )


TeslaDeaths("../data/tesla-deaths/Tesla Deaths.csv")
