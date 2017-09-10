import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick2_ohlc
%matplotlib inline

class SdZones:
    def __init__(self, data):
        self.data  = data

    def up_or_down(self):
        """this column will be true if the candle is up """
        self.data['up_down'] = np.where(self.data['Open'] > self.data['Close'], True, False)

    def body(self):
        """the body of the candle"""
        self.data['body'] = (self.data['Close'] - self.data['Open']).abs()

    def spread(self):
        """the spread of the candle"""
        self.data['spread'] = self.data['High'] - self.data['Low']


    def is_exciting_candle(self):
        self.data['is_exciting'] = self.data['body'] > (0.5*self.data['spread'])

    def clean(self):
        """removes unneeded columns"""
        self.data.drop(['up_down', 'body','spread'], axis=1, inplace= True)

    def run_all(self):
        """run all the methods"""
        self.up_or_down()
        self.body()
        self.spread()
        self.is_exciting_candle()
        self.clean()



"""
first determine all arias the have interesting boring interesting pattern ignore
all areas that the price broke into after the date of occurrence make sure to
have the data for the open high close low for all the boring candles area
so you can make the vis
"""





data = pd.read_csv('data/input/AAPL.csv').tail(70)
sample =  SdZones(data=data)
sample.run_all()
data = sample.data
def plot_boring_and_intersting(data):
    data.index = np.arange(data.shape[0])
    fig, ax = plt.subplots(figsize=(32,12))
    candlestick2_ohlc(ax,data['Open'],data['High'],data['Low'],data['Close'],width=0.6)
    plt.vlines(data.index[data['is_exciting']], data.Close.min(), data.Close.max(), alpha=0.2, colors='g')

plot_boring_and_intersting(data)
