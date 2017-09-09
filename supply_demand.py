import pandas as pd

class SdZones:
    def __init__(self, data):
        self.data  = data

    def exciting_candle(self):
        self.data['exciting_candle'] = (self.data['Open'] - self.data['Close']) > (0.5*(self.data['High'] - self.data['Low']))

    def boring_candle(self):
        self.data['boring_candle'] = (self.data['Open'] - self.data['Close']) <= (0.5*(self.data['High'] - self.data['Low']))

data = pd.read_csv('data/input/AAPL.csv')



sample =  SdZones(data=data)
sample.data.head()

sample.exciting_candle()
sample.boring_candle()
sample.data.head(20)
