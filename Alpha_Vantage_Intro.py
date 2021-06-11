#To get this code to work, in work terminal add your API to the following 'export ALPHAVANTAGE_API_KEY='
#Verfiy the variable has been set 'echo $ALPHAVANTAGE_API_KEY'
import requests
import os
import json
import pandas as pd 
from datetime import datetime
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators


app = TechIndicators(output_format='pandas')

#Get help for functions
#help(app.get_macd)


#Get locally stored api key and map to variable
api_key = os.getenv('ALPHAVANTAGE_API_KEY')


#Get info from the user
#print("Enter which function you want to query")
#function = input()
#print("Enter which ticker you want to query")
#symbol = input()

#Defining local variables
#base_url = 'https://www.alphavantage.co/query?'
#function = 'TIME_SERIES_DAILY_ADJUSTED'

function = 'SMA'
interval = 'weekly'
time_period = '10'
series_type = 'open'

symbol = 'IBM'
outputsize = 'compact'

#Send request with defined parameters
#&datatype=csv -to have a downloadable csv file
#response = requests.get(f'{base_url}function={function}&symbol={symbol}&outputsize={outputsize}&apikey={api_key}')
#print(response.json())

#response = requests.get(f'{base_url}function={function}&symbol={symbol}&interval=weekly&time_period=10&series_type=open&apikey={api_key}')
#print(response.json())




base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'FX_INTRADAY',
  'from_symbol': 'EUR',
  'to_symbol': 'USD', 
  'interval': '15min',
  'apikey': api_key}

response = requests.get(base_url, params=params)
response_dict = response.json()
_, header = response.json()

#Convert to pandas dataframe
df = pd.DataFrame.from_dict(response_dict[header], orient='index')

#Clean up column names
df_cols = [i.split(' ')[1] for i in df.columns]
df.columns = df_cols

df.set_index('timestamp', inplace=True) #Time-series index 

print(df)








#Clean the response to only obtain the latest result



#SHOP.TRT -supports different exchanges



