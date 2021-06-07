import requests
import os
from alpha_vantage.timeseries import TimeSeries

app = TimeSeries()

#Get my api key and map to variable
api_key = os.getenv('ALPHAVANTAGE_API_KEY')

#aapl = app.get_daily_adjusted('AAPL', outputsize='full')
#print(aapl)


base_url = 'https://www.alphavantage.co/query?'
function = 'TIME_SERIES_DAILY_ADJUSTED'
symbol = 'IBM'
outputsize = 'compact'

#Send request with defined parameters
response = requests.get(f'{base_url}function={function}&symbol={symbol}&outputsize={outputsize}&apikey={api_key}')
print(response.json())

#SHOP.TRT -supports different exchanges

#&datatype=csv -to have a downloadable csv file

