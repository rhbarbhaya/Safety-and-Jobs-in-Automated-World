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

    def read_files(self, directory, files):
        accident = pd.DataFrame()
        vehicle = pd.DataFrame()
        for file in files:
            if 'accident' in file.lower() :
                accident = pd.read_csv(os.path.join(directory, file), low_memory=False)
                if 'ST_CASE' in accident.columns:
                    
            if 'vehicle' in file.lower() :
                vehicle = pd.read_csv(os.path.join(directory, file), low_memory=False)
        _data_ = accident.merge(vehicle, left_on='ST_CASE', right_on='ST_CASE', how='left')


    def main(self):
        for directory, _, files in os.walk('../data/car-accident'):
            _data_ = self.read_files(directory, files)
            # print(_data_.head(1))

Car_Accident()
