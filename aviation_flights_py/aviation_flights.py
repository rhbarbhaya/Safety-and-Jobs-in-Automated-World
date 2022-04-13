"""
Project submission towards the ANLY 699 project
This project shows the flight information and getting some trend lines
"""
import os
import matplotlib.pyplot as plt
import pandas as pd


class Aviation:
	"""
	class declaration for access control
	"""
	def __init__(self) -> None:
		"""
		default class, calling on the main function to avoid running double scripts
		There are no return types for this function.
		"""
		self.main()

	@staticmethod
	def read_dataset(input_file_path) -> object:
		"""
		Read the csv file from the given input filepath
		Returns pandas dataframe object
		"""
		return pd.read_csv(input_file_path)

	@staticmethod
	def data_graph(df) -> None:
		"""
		creates a scatter graph based on the group by parameter for time with count as the objective for this project
		"""
		_data_ = df.groupby(by=['YEAR'], sort=True, as_index=True)['UNIQUE_CARRIER'].count().reset_index(name='Flights')
		plt.scatter(_data_['YEAR'], _data_['Flights'], label='Flights by year')
		plt.xlabel("Year")
		plt.ylabel("Flights")
		plt.title("Count of Flights by Major Airline(s) in the USA by Year")
		plt.legend()
		plt.show()
		return None

	def main(self, data_directory='../data/aviation-flights') -> None:
		_data_ = pd.DataFrame()
		for file in os.listdir(data_directory):
			_data_ = pd.concat([self.read_dataset(os.path.join(data_directory, file)), _data_])
		print("File Read Complete")
		self.data_graph(_data_)


aviation = Aviation()
