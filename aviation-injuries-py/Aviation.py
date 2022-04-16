"""Aviation database script, scopes, cleans and puts the dataset ready for consumption

Link: https://www.ntsb.gov/safety/data/Pages/Data_Stats.aspx
Author: Rushabh Barbhaya
"""
import datetime
import os
from sqlite3 import DataError
import pandas as pd
pd.set_option('mode.chained_assignment', None)

class Aviation:
    """Get the aviation data in the format and the scope and required fo the project
    The Project is to get the number of people injured by aviation accidents and the time
    to make a statement on aircraft industry and it's automation againts safety
    """
    def get_scope(self, scope_directory="../data/aviation-injuries"):
        """get the whole scope of the dataset that is required for the analysis

        Args:
            scope_directory (str, optional): get the data folder directory.
            Defaults to "./data".

        Returns:
            pandas.DataFrame: scoped dataframe for all the files in scope
        """
        master_data = pd.DataFrame()
        try:
            for folder, _, files in os.walk(scope_directory):
                for file in files:
                    if file.startswith('events'):
                        print(f"Read Complete --- {os.path.join(folder, file)}")
                        data_f = pd.read_csv(os.path.join(folder, file), low_memory=False)
                        print(f"Data Extracted --- {data_f.shape[0]} records found")
                        data_f = data_f[
                            [
                                'ev_id',
                                'ntsb_no',
                                'ev_state',
                                'ev_country',
                                'ev_year',
                                'ev_month',
                                'inj_f_grnd',
                                'inj_m_grnd',
                                'inj_s_grnd',
                                'inj_tot_f',
                                'inj_tot_m',
                                'inj_tot_n',
                                'inj_tot_s',
                                'inj_tot_t'
                            ]
                        ]
                        master_data = pd.concat([master_data, data_f])
            print("\n\n")
            print(f"Data read complete --- Total {master_data.shape[0]} \
                records across {master_data.shape[1]} columns")
            return master_data
        except Exception as error:
            raise DataError("Error reading data, BREAKING ISSUE") from error



    def country_scope(self, _data_, country=['USA']):
        """Scope the dataset based on a country filer, taken in a list argument of
        the country code that is in dataset.
        Please refer to the ct_iaids dataset for scope defiantion

        Args:
            _data_ (pandas.DataFrame): get the master DataFrame that is used for
            the scope mapping
            country (list, optional): list arguent for all the countries required
            for the scope. Defaults to ['USA'].

        Returns:
            pandas.DataFrame: returns the countries that are in scope
        """
        try:
            new_data = _data_[_data_['ev_country'].isin(country)]
            print(f"Scoping data to USA --- Removed {_data_.shape[0] - new_data.shape[0]} records")
            print(f"Total records --- {new_data.shape[0]} across {new_data.shape[1]} columns")
            return new_data
        except Exception as error:
            print("Error in processing records, NON_BREAKING")
            print(f"Error\n{error}")
            return _data_


    def state_scope(self, _data_, states=['AZ']):
        """Scope the dataset based on the states in a country filer, taken in a list
        argument of the states
        in a country code that is in dataset. Please refer to the ct_iaids dataset
        for scope defiantion

        Args:
            _data_ (pandas.DataFrame): Get the master DataFrame that is used for
            the scope mapping
            states (list, optional): all the args for state of the country that
            is in scope. Defaults to [].

        Returns:
            pandas.DataFrame: returns the states of the country that are in scope
        """
        try:
            new_data = _data_[_data_['ev_country'].isin(states)]
            print(f"Scoping data to USA --- Removed {_data_.shape[0] - new_data.shape[0]} records")
            print(f"Total records --- {new_data.shape[0]} across {new_data.shape[1]} columns")
            return new_data
        except Exception as error:
            print("Error in processing records, NON_BREAKING")
            print(f"Error\n{error}")
            return _data_


    def remove_dupes(self, _data_, key_column=['ev_id', 'ntsb_no']):
        """Function to remove duplicates from the dataset. Keys can be specified for the schema.

        Args:
            _data_ (pandas.DataFrame): The input data set from any previous step
            key_column (list, optional): primary keys in the dataset.
            Defaults to ['ev_id', 'ntsb_no'].

        Returns:
            pandas.DataFrame: DataFrame with duplicates removed
        """
        try:
            new_data = _data_.drop_duplicates(subset=key_column)
            print(f"{_data_.shape[0] - new_data.shape[0]} dupes found and removed")
            print(f"Total records --- {new_data.shape[0]} with {new_data.shape[1]} columns")
            return new_data
        except Exception as error:
            print("Error in processing records, NON_BREAKING")
            print(f"Error\n{error}")
            return _data_


    def total_injuries(
        self,
        _data_,
        ground_scope=['inj_f_grnd', 'inj_m_grnd', 'inj_s_grnd'],
        flight_scope=['inj_tot_f', 'inj_tot_m', 'inj_tot_s']
        ):
        """Calculate the injuries count for ground, flight and overall. scope is pre-fixed,
        can be changed on parameters

        Args:
            _data_ (pandas.DataFrame): scoped input for ETL
            ground_scope (list, optional): scope for ground injuries.
            Defaults to ['inj_f_grnd', 'inj_m_grnd', 'inj_s_grnd'].
            flight_scope (list, optional): scope for flight injuries.
            Defaults to ['inj_tot_f', 'inj_tot_m', 'inj_tot_s'].

        Returns:
            pandas.DataFrame: The same dataset with 3 additional columns, showing the ground,
            flight and total injuries
        """
        scope = ground_scope+flight_scope
        for key in scope:
            _data_[key] = pd.to_numeric(_data_[key], errors='coerce').fillna(0).astype(int)
        _data_['ground_injuries'] = _data_[ground_scope].sum(axis=1)
        print(f"Total Ground Injuries --- {_data_['ground_injuries'].sum(axis=0)}")
        _data_['flight_injuries'] = _data_[flight_scope].sum(axis=1)
        print(f"Total Flight Injuries --- {_data_['flight_injuries'].sum(axis=0)}")
        _data_['total_injuries'] = _data_['ground_injuries'] + _data_['flight_injuries']
        print(f"Overall Injuries --- {_data_['total_injuries'].sum(axis=0)}")
        return _data_


    def setup_init(self):
        """initial print setup for clean view
        """
        print()
        print("-"*65)
        print("\tHarrisburg School of Science and Technology\t")
        print("\tANLY-699: Dr. Roozbeh Sadeghian\t")
        print("\tRushabh Barbhaya, RBarbhaya@my.harrisburgu.edu\t")
        print(f"\t{datetime.datetime.now().strftime('%c')}\t")
        print()
        print()
        print("\tAUTOMATION IN DAILY LIFE")
        print()
        print("Starting log\n\n")
        return


    def get_master_set(self):
        """main block for controlling the whole application.

        Returns:
            pandas.DataFrame: masters dataframe for analysis
        """
        self.setup_init()
        master_data = self.get_scope()
        print(master_data.shape)
        country_scoped = self.country_scope(master_data)
        print(country_scoped.shape)
        dupes_removed = self.remove_dupes(country_scoped)
        print(dupes_removed.shape)
        master = self.total_injuries(dupes_removed)
        print(f"dataset shape --- {master.shape}")
        print("-"*65)
        return master
