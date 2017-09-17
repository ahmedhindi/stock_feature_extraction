import pandas as pd
import numpy as np
import stockstats
from os import listdir
from stockstats import StockDataFrame as Sdf
from timaker import TiMaker
import sys
import warnings

pd.options.mode.chained_assignment = None
warnings.simplefilter(action='ignore', category=FutureWarning)



def get_all_json_files():
    """Return the path + json file name."""
    all_files = [i for i in listdir("data/input") if i.endswith('.csv')]
    return all_files, dir_c, dir_s


def main():

    arg = sys.argv[1].split("=")[0]
    if  arg in ['file', 'all']:
        if arg == 'file':
            path = sys.argv[1].split("=")[1]
            make_csvs(path=path)

        elif arg == 'all':

            for i in [i for i in listdir("data/input") if i.endswith('.csv')]:
                make_csvs(path=i)

    else:
        print('please enter the right argument file="file name" to work wih one file or or all')
        print('example~$ python main.py all')
        print('example~$ python main.py file="apple.csv"')

def make_csvs(path):
    ti = TiMaker(path)
    ti.run_all()
    ti.final_data = ti.final_data.round(3)
    ti.final_data['stock_name'] = path.split(".")[0]
    ti.save_df()

if __name__ == '__main__':
    main()
