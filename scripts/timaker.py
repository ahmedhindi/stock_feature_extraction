import pandas as pd
import numpy as np
import stockstats
from stockstats import StockDataFrame as Sdf
pd.options.mode.chained_assignment = None


class TiMaker():
    def __init__(self, data):
        """
        data: the data of the csv file containing stock data.
        """
        self.features = {
        "Stocastic":['kdjd_5','kdjk_3'],
        "RSI":['rsi_14'],
        "ADX":['adx_15_ema'],
        # "MACD":['macd', 'macds', 'macdh'],
        "BBands":['boll', 'boll_ub', 'boll_lb'],
        "ATR":['atr'],}
        self.data = data
        self.stockdf = None
        self.col_names = None
        self.final_data = None
        self.sma_list = [20,50,200]

    def macd(self, n_fast=12, n_slow=26):
        EMAfast = pd.Series(pd.ewma(self.stockdf['close'], span = n_fast, min_periods = n_slow - 1))
        EMAslow = pd.Series(pd.ewma(self.stockdf['close'], span = n_slow, min_periods = n_slow - 1))
        MACD = pd.Series(EMAfast - EMAslow, name = 'macd_' + str(n_fast) + '_' + str(n_slow))
        MACDsign = pd.Series(pd.ewma(MACD, span = 9, min_periods = 8), name = 'macdsign_' + str(n_fast) + '_' + str(n_slow))
        MACDdiff = pd.Series(MACD - MACDsign, name = 'macddiff_' + str(n_fast) + '_' + str(n_slow))
        self.stockdf[MACD.name] = MACD
        self.stockdf[MACDsign.name] = MACDsign
        self.stockdf[MACDdiff.name] = MACDdiff
        for i in [MACD.name, MACDsign.name, MACDdiff.name]:
            self.col_names.append(i)

    def read_df(self):
        """Read csv stock data and convert it to stock data frame."""
        self.stockdf = Sdf.retype(pd.read_csv('data/input/'+self.data))
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

    def make_smas(self):
        for i in self.sma_list:
            name = str(i)+'_sma'
            self.col_names.append(name)
            self.stockdf[name]  = self.stockdf['close'].rolling(i).mean()

    def run_all(self):
        """Run all functions and return the final dataframe."""
        self.read_df()
        self.make_smas()
        self.macd()
        self.feature_maker()
        self.make_final_data()
        return self.final_data

    def save_df(self):
        """save the df as a csv"""
        self.final_data.to_csv('data/output/new_{}'.format(self.data))
