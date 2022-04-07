import pandas as pd
import os

main_data_folder = r"data"
for folder in os.listdir(main_data_folder):
    if not folder.startswith("."):
        data_folder = os.path.join(main_data_folder, folder)
        for i in os.listdir(data_folder):
            if not i.startswith("."):
            # print(os.path.join(data_folder, i))
                try:
                    df = pd.read_csv(os.path.join(data_folder, i), sep=",", low_memory=False)
                    print(f"Read successful --- {os.path.join(data_folder, i)} --- shape {df.shape} ")
                except UnicodeDecodeError as e:
                    print(f"Error opening {os.path.join(data_folder, i)} --- Reason {e}")
    # print(df.head())