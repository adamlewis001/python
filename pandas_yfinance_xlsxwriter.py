# pull stock quotes for multiple symbols and save the data to an existing csv file

import yfinance as yf
import xlsxwriter as xl
import pandas as pd
from datetime import datetime
from datetime import timedelta

dt_start = "2005-01-01"
dt_tomorrow = datetime.today() + timedelta(days=1)
dt_end = rb_tomorrow.strftime('%Y-%m-%d')

data = yf.download("AAPL TSLA AMZN NFLX", start = dt_start, end = dt_end)

df = data['Close']

df.to_csv('spreadsheet.csv', encoding='utf-8')
