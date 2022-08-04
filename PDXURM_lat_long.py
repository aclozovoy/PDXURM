import numpy as np
import pandas as pd
import googlemaps
gmaps = googlemaps.Client(key='API_KEY_GOES HERE')
from datetime import datetime
import time


# IMPORT DATA
df = pd.read_excel('URM_ALL_2020_05_15_12_07_46.xlsx')
df['LONG_ADDRESS'] = df['ADDRESS'] + ' PORTLAND OREGON'

# ADD LONG AND LAT COLUMNS
df['LONG'] = ""
df['LAT'] = ""



# TEST DATA
df2 = pd.DataFrame({'LONG_ADDRESS': ['104 San Felipe Way Novato', '172 Highland San Luis Obispo', '2568 NW Vaughn Portland']})
df2['LONG'] = ""
df2['LAT'] = ""


# Geocoding an address
for x in range(len(df)):
    try:
        time.sleep(0.5) # to add delay in case of large DFs
        geocode_result = gmaps.geocode(df['LONG_ADDRESS'][x])
        df['LAT'][x] = geocode_result[0]['geometry']['location']['lat']
        df['LONG'][x] = geocode_result[0]['geometry']['location']['lng']
        print(x+1 , '/' , len(df) , ' complete.')
    except IndexError:
        print("Address was wrong...")
    except Exception as e:
        print("Unexpected error occurred.", e )


# OUTPUT TO CSV
df.to_csv('URM_DATA.csv')

# OUTPUT TO XLSX
df.to_excel('URM_DATA.xlsx')