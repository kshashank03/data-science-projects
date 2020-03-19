import googlemaps #Make sure you install this on your computer
import pandas as pd
from tqdm import tqdm #Progress bar to track iterations

#Set up the API
API_KEY = #Insert API key
gmaps = googlemaps.Client(key=API_KEY)

#Imports your Excel file to iterate over
filename = #Insert filename here
df = pd.read_excel(filename, sheet_name='#Insert sheetname here)

#Creates two empty lists to store lats and longs from the API respectively
latitude = []
longitude = []

#Iterates over a single column with full addresses and outputs the lat and long into two lists
for index, row in tqdm(df.iterrows()):
    geocode_result = gmaps.geocode(row['Location'])
    latitude.append(geocode_result[0]["geometry"]["location"]["lat"])
    longitude.append(geocode_result[0]["geometry"]["location"]["lng"])

#Adds the two new columns to the end of the spreadsheet    
df['latitude'] = latitude
df['longitude'] = longitude

#Output results to a file
df.to_excel(#Put output location here, index=None)
