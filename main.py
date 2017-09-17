import pandas as pd
import numpy as np
import stockstats
from os import listdir
from stockstats import StockDataFrame as Sdf
import sys
import warnings
#################
from scripts.candles2 import MakeCandles
from scripts.strategy import Strategy
from  scripts.timaker import TiMaker
pd.options.mode.chained_assignment = None
warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    # read all the files in the input file
    output_file = 'data/output/'
    input_file = 'data/input/'
    print("reading the data from the input folder.....")

    all_files = get_all_csv_files()

    for i in all_files:
        # run the TI nd stratigy script
            # save with prefix  I

        ti = TiMaker(i+'.csv')
        ti_ = ti.run_all()
        # print(ti.head())
        # ti_.to_csv(f'{output_file}(T)_{i}.csv')
        ####################
        st = Strategy(ti.final_data)
        st = st.runall()
        st.to_csv(f'{output_file}(I)_{i}.csv')
        #####################
        # run candle
            # prefix C
        candles = MakeCandles(i+'.csv')
        candles.run_all()
        candles.data.to_csv(f'{output_file}(C)_{i}.csv')
        # print(candles.data.head())
        # run supply and demand
            # prefix SD



def get_all_csv_files():
    """Return the path + csv file name."""
    all_files = [i.split('.')[0] for i in listdir("data/input") if i.endswith('.csv')]
    return all_files




if __name__ == '__main__':
    main()
