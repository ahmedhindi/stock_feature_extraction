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
    ti.final_data = ti.final_data.round(3)
    ti.final_data['stock_name'] = path.split(".")[0]
    print(ti.final_data.head())
    ti.save_df()



if __name__ == '__main__':
    main()
