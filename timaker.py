import pandas as pd
import numpy as np
import stockstats
from stockstats import StockDataFrame as Sdf


class TiMaker():
    def __init__(self, path):
        """
        path: the path of the csv file containing stock data.
        """
        self.features = {
        "Stocastic":['kdjd_5','kdjk_3'],
        "RSI":['rsi_14'],
        "ADX":['adx_15_ema'],
        "MACD":['macd', 'macds', 'macdh'],
        "BBands":['boll', 'boll_ub', 'boll_lb'],
        "ATR":['atr'],}
        self.path = path
        self.stockdf = None
        self.col_names = None
        self.final_data = None

    def read_df(self):
        """Read csv stock data and convert it to stock data frame."""
        self.stockdf = Sdf.retype(pd.read_csv('data/input/'+self.path))
        self.col_names = list(self.stockdf.columns)

    def feature_maker(self):
        """Make features"""
        #loop over the keys of the features dict
        for ind in self.features.keys():
            #loop over the commands in the value (list) for the ind key
            for comm in self.features[ind]:
                col_name = str(ind+'_'+comm)
                #append the new features to the col_names list
                self.col_names.append(col_name)
                #creat  new feature as a column in the datafame
                self.stockdf[col_name] = self.stockdf.get(comm)

    def make_final_data(self):
        """The final dataframe."""
        self.final_data = self.stockdf[self.col_names].replace(10.000000,np.nan).dropna()

    def run_all(self):
        """Run all functions and return the final dataframe."""
        self.read_df()
        self.feature_maker()
        self.make_final_data()

    def save_df(self):
        """save the df as a csv"""
        self.final_data.to_csv('data/output/new_{}'.format(self.path))
