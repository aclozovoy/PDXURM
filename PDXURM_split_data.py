import numpy as np
import pandas as pd


# IMPORT DATA
# df = pd.read_csv('URM_DATA.csv')
df = pd.read_excel('URM_DATA.xlsx')

# SHOW 'UPGRADE_STATUS' TYPES AND COUNTS
types = df.groupby('UPGRADE_STATUS')['ADDRESS'].count()
print(types)

# SORT DATA AND SAVE AS CSV - FULL
df_full = df[df['UPGRADE_STATUS'] == 'FULL']
df_full.to_csv('URM_DATA_FULL.csv')
df_full.to_excel('URM_DATA_FULL.xlsx')

# SORT DATA AND SAVE AS CSV - PARTIAL
df_partial = df[df['UPGRADE_STATUS'] == 'PARTIAL']
df_partial.to_csv('URM_DATA_PARTIAL.csv')
df_partial.to_excel('URM_DATA_PARTIAL.xlsx')

# SORT DATA AND SAVE AS CSV - REROOF
df_reroof = df[df['UPGRADE_STATUS'] == 'REROOF']
df_reroof.to_csv('URM_DATA_REROOF.csv')
df_reroof.to_excel('URM_DATA_REROOF.xlsx')

# SORT DATA AND SAVE AS CSV - UNKNOWN
df_unknown = df[df['UPGRADE_STATUS'] == 'UNKNOWN']
df_unknown.to_csv('URM_DATA_UNKNOWN.csv')
df_unknown.to_excel('URM_DATA_UNKNOWN.xlsx')
