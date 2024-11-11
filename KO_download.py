# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:00:43 2024

@author: santi
"""

import yfinance as yf
import datetime
import pandas as pd
import os
     
# Ticker para cocaola
ticker = 'KO'
#end_date = datetime.datetime.now()
#start_date = end_date - datetime.timedelta(days=365)
data = yf.download(ticker, period = '10y', interval = '1d')
data.to_csv('ko_10years.csv')
