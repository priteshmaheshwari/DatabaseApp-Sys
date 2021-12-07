import io
import csv
import math
import psycopg2
import numpy as np
import pandas as pd
import json as simplejson
from pymongo import MongoClient
from sqlalchemy import create_engine
#import database


		
engine = create_engine('postgresql+psycopg2://nyc_covid:nyc_covid@localhost:5432/nyc_covid')

hospital_df= pd.read_csv('./data/hospital_data.csv')
hospital_df.to_sql('hospital_data', engine, if_exists='append', index=False)

metadata_df= pd.read_csv('./data/metadata.csv')
metadata_df.to_sql('metadata', engine, if_exists='append', index=False)

contact_df = pd.read_csv('./data/contact_data.csv')
contact_df.to_sql('contact_data', engine, if_exists='append', index=False)

address_df = pd.read_csv('./data/address_data.csv')
address_df.to_sql('address_data', engine, if_exists='append', index=False)

cases_df = pd.read_csv('./data/us-counties-2021.csv')
cases_df.to_sql('counties', engine, if_exists='append', index=False)


print('data loaded successfully')
						