import talib
import pandas as pd
import pickle

class MakeCandles:
    def __init__(self, name):
        self.name = name
        self.info = MakeCandles.read_dict()
        self.path = 'data/input/'
        self.data = None

    def read_csv(self):
        """Reads the data with the indicators as columns (from the output file)"""
        dfn = self.path + self.name
        self.data = pd.read_csv(dfn, index_col=0)
        self.data.columns = self.data.columns.str.title()

    @staticmethod
    def read_dict():
        with open('pickledDict.p', 'rb') as f:
            return pickle.load(f)

    def make_all_pattern(self):
        O,H,L,C = (self.data.Open.values, self.data.High.values, self.data.Low.values, self.data.Close.values)
        for i in self.info:
            temp =  f'talib.{i}(O,H,L,C)'
            pattern_array =  eval(temp)
            self.data[self.info[i]] = pattern_array

    @staticmethod
    def map_to_true_false(r):
        if r == 0:
            return False
        else:
            return True

    def clean_data(self):
        self.data.iloc[:,6:] = self.data.iloc[:,6:].applymap(MakeCandles.map_to_true_false)

    def run_all(self):
        self.read_csv()
        self.make_all_pattern()
        self.clean_data()


"""a = MakeCandles(pd.read_csv('data/input/AAPL.csv', index_col=0))
a.run_all()
a.data.to_csv('candles.csv')"""
