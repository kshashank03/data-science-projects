import numpy as np
import pandas as pd
import os
from tqdm import tqdm

dir_path = os.path.dirname(os.path.realpath(__file__))

print("\n\n\n\n\nThis tool uses the NHTSA's Vehicle API to tell you all \nof the models released by a given manufacturer in a given year.\n\n\n\n\n")
print("What make of car do you want?")
input_make = input()

print("What is the minimum year you want to download data from?")
input_min_year = input()

print("What is the maximum year you want to download data from?")
input_max_year = input()

def data_download(make, min_year, max_year, new_dataframe):

    for min_year in tqdm(range(min_year, max_year + 1)):
        base_url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/"
        year = str(min_year)
        url = base_url + make + "/modelyear/" + year + "?format=csv"
        car_data = pd.read_csv(url)
        car_data_df = pd.DataFrame(data=car_data)
        car_data_df['Year'] = min_year
        min_year += 1
        new_dataframe = new_dataframe.append(car_data_df, ignore_index=True)
        if min_year == max_year + 1:
            new_dataframe.to_excel(dir_path + "/"+ make + "_Model_Data.xlsx", index=False)
            print("File saved to: " + dir_path + "/"+ make + "_Model_Data.xlsx")


data_download(input_make, int(input_min_year), int(input_max_year), new_dataframe = pd.DataFrame(np.array([[]])))