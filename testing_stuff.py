import pandas as pd 
import numpy as np

data = pd.read_csv('data/input/AAPL.csv', index_col=0)

data.head()


a = (data['Open'] == data['Close'])
a.head()

""" Bullish Engulfing
((O1 > C1) AND (C > O) AND (C >= O1) AND (C1 >= O) AND ((C - O) > (O1 - C1)))"""
a = ((data['Open'].shift(1) > data['Close'].shift(1)) & (data['Close'] > data['Open']) & (data['Close'] >= data['Open'].shift(1)) & (data['Close'].shift(1) >= data['Open']) & ((data['Close']-data['Open']) > (data['Open'].shift(1)-data['Close'].shift(1))))
a.head()
