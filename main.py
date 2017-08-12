import pandas as pd
import numpy as np
import stockstats
from stockstats import StockDataFrame as Sdf
from timaker import TiMaker
import sys


def main():
    path = sys.argv[1].split("=")[1]
    ti = TiMaker(path)
    ti.run_all()
    print(ti.final_data.head())
    ti.save_df()



if __name__ == '__main__':
    main()
