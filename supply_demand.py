import pandas as pd
import numpy as np

class SdZones:
    def __init__(self, data):
        self.data  = data

    def up_or_down(self):
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
first determine all arias the have interesting boring interesting pattern
ignore all areas that the price broke into after the date
of occurrence make sure to have the data for the
open high close low for all the boring candles area so you can make the vis
"""




data = pd.read_csv('data/input/AAPL.csv')



sample =  SdZones(data=data)
sample.data.head()

sample.exciting_candle()
sample.boring_candle()
sample.data.head(20)
