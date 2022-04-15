"""
This module is for the cars involved in accidents dataset
https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/
https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars
"""
import os
import pandas as pd
import matplotlib.pyplot as plt


class CarAccident:
    def __init__(self):
        self.main()

    def read_files(self, directory, files):
        for file in files:
            if 'accident' in file.lower():
                accident = pd.read_csv(os.path.join(directory, file), low_memory=False)
                accident['ST_CASE'] = accident['ST_CASE'].astype(str)
                accident['YEAR'] = ''.join(filter(lambda i: i.isdigit(), os.path.basename(directory)))
                accident = accident[['ST_CASE', 'MONTH', 'YEAR', 'FATALS']]
                return accident
        return None

    def data_graph(self, data):
        _data_ = data.groupby(by=['YEAR'], sort=True, as_index=True)['FATALS'].sum().reset_index(name='FATALS')
        plt.scatter(_data_['YEAR'], _data_['FATALS'], label='Car fatalities by year')
        plt.xlabel("Year")
        plt.ylabel("Car Fatalities")
        plt.title("Car fatalities in the USA by Year")
        plt.tick_params(axis='x', rotation=90)
        plt.legend()
        plt.show()

    def main(self):
        stack_data = pd.DataFrame()
        for directory, _, files in os.walk('../data/car-accident'):
            if '.DS_Store' in files:
                pass
            else:
                accident = self.read_files(directory, files)
                stack_data = pd.concat([stack_data, accident])
        self.data_graph(stack_data)

CarAccident()
