
import os
import matplotlib.pyplot as plt
import pandas as pd

class aviation:
	def __init__(self) -> None:
		self.main()
		return None

	def read_dataset(self, input_file_path) -> object:
		return pd.read_csv(input_file_path)

	def data_graph(self, df) -> None:
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


aviation = aviation()
