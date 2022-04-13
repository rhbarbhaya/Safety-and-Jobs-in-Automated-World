"""
This module is for the cars involved in accidents dataset
https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/
https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars
"""
import os
import pandas as pd


class Car_Accident:
    def __init__(self):
        self.main()

    def read_files(self, input_file_path):
        try:
            return pd.read_csv(input_file_path, low_memory=False)
        except UnicodeDecodeError:
            print(input_file_path)

    def main(self):
        for directory, folder, files in os.walk('../data/car-accident'):
            for file in files:
                if 'accident' in file.lower():
                    accident = self.read_files('../data/car-accident/FARS1975NationalCSV/'+file)
                if 'vehicle' in file.lower():
                    vehicle = self.read_files('../data/car-accident/FARS1975NationalCSV/' + file)
            _data_ = pd.merge(accident, vehicle, on='ST_CASE')

Car_Accident()
