import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None


class Strategy:

    def __init__(self, file):
        self.file = file
        self.path = 'data/output/'

    def read_csvs(self):
        """Reads the data with the indicators as columns (from the output file)"""
        self.data = pd.read_csv(self.path+self.file)

    def save_data(self):
        """Saves the file in the file strategy"""
        self.data.to_csv('data/strategy/strategy_{}'.format(self.file.replace('new_','')))

    def stocastic(self):
        """ The rules for stocastics."""
        sd = [i for i in self.data.columns if 'kdjd' in i][0]
        sk = [i for i in self.data.columns if 'kdjk' in i][0]

        st = self.data[[sd, sk]]
        # K<D
        st['k<d'] = st[sk] <  st[sd]
        st['shifted'] = st['k<d'].shift(1)
        self.data['SKDT'] = np.where((st['k<d'] == True) & (st['shifted'] == False), True,False)
        # -----------
        # K>D
        st['k>d'] = st[sk] >  st[sd]
        st['shifted'] = st['k>d'].shift(1)
        self.data['SKDB'] = np.where((st['k>d'] == True) & (st['shifted'] == False), True,False)
        # ----------
        #########################%k################
        #"SOBZEK">>>Over Bought zone entry
        OB = st[sk] > 80
        OB_shifted = OB.shift(1)
        self.data['SOBZEK'] = np.where((OB==True)&(OB_shifted==False), True,False)
        # ---------------
        #"SOBZXK">>>Over Bought zone exit
        OB = st[sk] < 80
        OB_shifted = OB.shift(1)
        self.data['SOBZXK'] = np.where((OB==True)&(OB_shifted==False), True,False)
        #  --------------
        #"SOSZEK">>>Over sold zone entry
        OS = st[sk] < 20
        OS_shifted = OS.shift(1)
        self.data['SOSZEK'] = np.where((OS==True)&(OS_shifted==False), True,False)
        # ---------------------
        #"SOSZXK">>>Over sold zone exit
        OS = st[sk] > 20
        OS_shifted = OS.shift(1)
        self.data['SOSZXK'] = np.where((OS==True)&(OS_shifted==False), True,False)

        #---------------------------
        #######################%D###################

        #"SOBZED">>>Over Bought zone entry
        OB = st[sd] > 80
        OB_shifted = OB.shift(1)
        self.data['SOBZED'] = np.where((OB==True)&(OB_shifted==False), True,False)
        # ---------------
        #"SOBZXD">>>Over Bought zone exit
        OB = st[sd] < 80
        OB_shifted = OB.shift(1)
        self.data['SOBZXD'] = np.where((OB==True)&(OB_shifted==False), True,False)
        #  --------------
        #"SOSZED">>>Over sold zone entry
        OS = st[sd] < 20
        OS_shifted = OS.shift(1)
        self.data['SOSZED'] = np.where((OS==True)&(OS_shifted==False), True,False)
        # ---------------------
        #"SOSZXD">>>Over sold zone exit
        OS = st[sd] > 20
        OS_shifted = OS.shift(1)
        self.data['SOSZXD'] = np.where((OS==True)&(OS_shifted==False), True,False)
        #--------------------------


    def rsi(self):
        """ The rules for RSI."""
        rsi_col = [i for i in self.data.columns if 'rsi' in i][0]
        rsi = self.data[rsi_col]

        # ----------
        #"RSIUE">>>RSI Upper band entry
        OB = rsi > 70
        OB_shifted = OB.shift(1)
        self.data['RSIUE'] = np.where((OB==True)&(OB_shifted==False), True,False)
        # ---------------
        # "RSIUX">>>RSI Upper band exit
        OB = rsi < 70
        OB_shifted = OB.shift(1)
        self.data['RSIUX'] = np.where((OB==True)&(OB_shifted==False), True,False)
        #  --------------
        # "RSILE">>>RSI Lower band entry
        OS = rsi < 30
        OS_shifted = OS.shift(1)
        self.data['RSILE'] = np.where((OS==True)&(OS_shifted==False), True,False)
        # ---------------------
        # "RSILX">>>RSI Lower band exit
        OS = rsi > 30
        OS_shifted = OS.shift(1)
        self.data['RSILX'] = np.where((OS==True)&(OS_shifted==False), True,False)

    def smas(self):
        """ The rules for moving avrages crossover."""
        _20 = [i for i in self.data.columns if '20' in i][0]
        _50 = [i for i in self.data.columns if '50' in i][0]
        _200 = [i for i in self.data.columns if '200' in i][0]


        # "PC20T" >>>> Price crosses 20DMA from TOP
        ps20 = self.data.close <  self.data[_20]
        ps20shifted = ps20.shift(1)
        self.data['PC20T'] = np.where((ps20 == True) & (ps20shifted == False), True,False)

        # "PC20B" >>>> Price crosses 20DMA from Bottom
        ps20 = self.data.close >  self.data[_20]
        ps20shifted = ps20.shift(1)
        self.data['PC20B'] = np.where((ps20 == True) & (ps20shifted == False), True,False)

        # "PC50T" >>>> Price crosses 50DMA from TOP
        ps50 = self.data.close <  self.data[_50]
        ps50shifted = ps50.shift(1)
        self.data['PC50T'] = np.where((ps50 == True) & (ps50shifted == False), True,False)

        # "PC50B" >>>> Price crosses 50DMA from Bottom
        ps50 = self.data.close >  self.data[_50]
        ps50shifted = ps50.shift(1)
        self.data['PC20B'] = np.where((ps50 == True) & (ps50shifted == False), True,False)

        # "PC200T" >>>> Price crosses 200DMA from TOP
        ps200 = self.data.close <  self.data[_200]
        ps200shifted = ps200.shift(1)
        self.data['PC200T'] = np.where((ps200 == True) & (ps200shifted == False), True,False)

        # "PC200B" >>>> Price crosses 200DMA from Bottom
        ps200 = self.data.close >  self.data[_200]
        ps200shifted = ps200.shift(1)
        self.data['PC200B'] = np.where((ps200 == True) & (ps200shifted == False), True,False)

        # "20C50T" >>>> 20DMA crosses 50DMA from Top
        _20t_50 = data[_20] <  self.data[_50]
        _20t_50_shifted = _20t_50.shift(1)
        self.data['20C50T'] = np.where((_20t_50 == True) & (_20t_50_shifted == False), True,False)

        # "20C50B" >>>> 20DMA crosses 50DMA from Bottom
        _20b_50 = data[_20] >  self.data[_50]
        _20b_50_shifted = _20b_50.shift(1)
        self.data['20C50B'] = np.where((_20b_50 == True) & (_20b_50_shifted == False), True,False)

        # "50C200T" >>>> 50DMA crosses 200DMA from Top
        _50t_200 = data[_50] <  self.data[_200]
        _50t_200_shifted = _50t_200.shift(1)
        self.data['50C200T'] = np.where((_50t_200 == True) & (_50t_200_shifted == False), True,False)

        # "50C200B" >>>> 50DMA crosses 200DMA from Bottom
        _50b_200 = data[_50] >  self.data[_200]
        _50b_200_shifted = _50b_200.shift(1)
        self.data['50C200B'] = np.where((_50b_200 == True) & (_50b_200_shifted == False), True,False)

        # "20C200T" >>>> 20DMA crosses 200DMA from Top
        _20t_200 = data[_20] <  self.data[_200]
        _20t_200_shifted = _20t_200.shift(1)
        self.data['20C200T'] = np.where((_20t_200 == True) & (_20t_200_shifted == False), True,False)

        # "20C200B" >>>> 20DMA crosses 200DMA from Bottom
        _20b_200 = data[_20] >  self.data[_200]
        _20b_200_shifted = _20b_200.shift(1)
        self.data['20C200B'] = np.where((_20b_200 == True) & (_20b_200_shifted == False), True,False)

    def bbands(self):
        """ The rules for Bollinger bands."""
        sub = self.data[[i for i in self.data.columns if 'bbands' in i]]
        lower_band = sub.bbands_boll_lb
        upper_band = sub.bbands_boll_ub
        high = self.data.high
        low = self.data.low

        # Bollinger band

        # "UBB1">>>Prie at Upper Bolliner band
        price_ubb = high == upper_band
        price_ubb_shifted = price_ubb.shift(1)
        self.data['UBB1'] = np.where((price_ubb == True) & (price_ubb_shifted == False), True,False)

        # "UBB2">>>Prie above Upper Bolinger bankd
        price_ubb = high > upper_band
        price_ubb_shifted = price_ubb.shift(1)
        self.data['UBB2'] = np.where((price_ubb == True) & (price_ubb_shifted == False), True,False)

        # "LBB1">>>Prie at Lower Bolliner band
        price_lbb = low == lower_band
        price_lbb_shifted = price_lbb.shift(1)
        self.data['LBB1'] = np.where((price_lbb == True) & (price_lbb_shifted == False), True,False)

        # "LBB2">>>Prie above Lower Bolinger bankd
        price_lbb = low < lower_band
        price_lbb_shifted = price_lbb.shift(1)
        self.data['LBB2'] = np.where((price_lbb == True) & (price_lbb_shifted == False), True,False)

    def macd(self):
        """ The rules for MACD."""
        sample = self.data[[i for i in self.data.columns if 'macd' in i]]
        sigh = sample.macdsign_12_26
        macd = sample.macd_12_26
        price_lbb = sigh < macd
        price_lbb_shifted = price_lbb.shift(1)
        self.data['SigmacdT'] = np.where((price_lbb == True) & (price_lbb_shifted == False), True,False)

        price_lbb = sigh > macd
        price_lbb_shifted = price_lbb.shift(1)
        self.data['SigmacdB'] = np.where((price_lbb == True) & (price_lbb_shifted == False), True,False)

    def usage(self):
        print("""
        note(a is the instance)
            a.read_csvs()
            a.stocastic()
            a.rsi()
            a.bbands()
            a.macd()
            a.save_data()
            or you can use a.runll() and it will do the same.
        """)

    def runall(self):
        self.read_csvs()
        self.stocastic()
        self.rsi()
        self.bbands()
        self.macd()
        self.save_data()


a = Strategy(file='new_AAPL.csv')
a.usage()
