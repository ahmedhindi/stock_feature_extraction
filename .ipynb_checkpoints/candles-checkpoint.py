import pandas as pd
import numpy as np

class CR:
    def __init__(self, name):
        self.name = name
        self.path = 'data/input/'
        self.data = None

    def read_csvs(self):
        """Reads the data with the indicators as columns (from the output file)"""
        self.data = pd.read_csv(self.path+self.name, index_col=0)

    def save_data(self):
        """Saves the file in the file strategy"""
        self.data.to_csv('data/candle/{}'.format(self.name))

    def doji(self):
        """Doji
        (O = C)"""
        return(self.data['Open'] ==  self.data['colse'])

    def doji_yesterday(self):
        """Doji Yesterday
        (O1 = C1)"""
        return(self.data['Open'].shift(1) == self.data['Close'].shift(1))

    def doji_and_near_doji(self):
        """Doji and Near Doji
        (ABS(O - C ) <= ((H - L ) * 0.1))"""
        return(((self.data['Open'] - self.data['Close']).abs()) <= ((self.data['High'] - self.data['Low']) * 0.1))

    def bullish_engulfing(self):
        """ Bullish Engulfing
        ((O1 > C1) AND (C > O) AND (C >= O1) AND (C1 >= O) AND ((C - O) > (O1 - C1)))"""
        return((self.data['Open'].shift(1) > self.data['Close'].shift(1)) and \
        (self.data['Close'] > self.data['Open']) and \
        (self.data['Close'] >= self.data['Open'].shift(1)) and \
        (self.data['Close'].shift(1) >= self.data['Open']) and \
        ((self.data['Close']-self.data['Open']) > (self.data['Open'].shift(1)-self.data['Close'].shift(1))))

    def bearish_engulfing(self):
        """Bearish Engulfing
        ((C1 > O1) AND (O > C) AND (O >= C1) AND (O1 >= C) AND ((O - C) > (C1 - O1)))"""
        return((self.data['Close'].shift(1) > self.data['Open'].shift(1)) and\
        (self.data['Open'] > self.data['Close']) and \
        (self.data['Open'] >= self.data['Close'].shift(1)) and \
        (self.data['Open'].shift(1) >= self.data['Close']) and \
        ((self.data['Open']-self.data['Close']) > (self.data['Close'].shift(1)-self.data['Open'].shift(1))))

    def hammer(self):
        """Hammer
        (((H-L)>3*(O-C)AND((C-L)/(.001+H-L)>0.6)AND((O-L)/(.001+H-L)>0.6)))"""
        return(((self.data['High'] - self.data['Low']) > ((self.data['Open']-self.data['Close'])*3)) and \
        ((self.data['Close']-self.data['Low']) / ((.001+self.data['High']-self.data['Low']) > 0.6)) and \
        ((self.data['Open'] - self.data['Low']) / (.001+self.data['High']-self.data['Low']) > 0.6))

    def hanging_man(self):
        """ Hanging Man
        (((H - L) > 4 * (O - C)) AND ((C - L) /
        (.001 + H - L) >= 0.75) AND ((O - L) / (.001 + H - L) >= .075)))"""
        return(((self.data['High'] - self.data['Low']) > ((self.data['Open'] - self.data['Close'])*4)) and \
        ((self.data['Close'] - self.data['Low']) / ((.001 + self.data['High'] - self.data['Low']) >= 0.75)) and\
        ((self.data['Open'] - self.data['Low']) / ((.001 + self.data['High'] - self.data['Low']) >= .075)))

    def pricing_line(self):
        """Piercing Line
        ((C1 < O1) AND (((O1 + C1) / 2) < C) AND (O < C) AND
        (O < C1) AND (C < O1) AND ((C - O) / (.001 + (H - L)) > 0.6))"""
        return(((self.data['Close'].shift(1)) < (self.data['Open'].shift(1))) and \
        (((self.data['Open'].shift(1) + self.data['Close'].shift(1)) / 2) < (self.data['Close'])) and \
        ((self.data['Open'] < self.data['Close']) and (self.data['Open'] < self.data['Close'].shift(1))) and \
        (self.data['Close'] < self.data['Open'].shift(1)) and \
        ((self.data['Close'] - self.data['Open']) / (0.001 + (self.data['High'] - self.data['Low'])) > 0.6))

    def dark_cloud(self):
        """Dark Cloud
        ((C1 > O1) AND (((C1 + O1) / 2) > C) AND (O > C) AND (O > C1) AND (C > O1)
        AND ((O - C) / (.001 + (H - L)) > .6))"""
        return((self.data['Close'].shift(1) > self.data['Open'].shift(1)) and \
        (((self.data['Close'].shift(1) + self.data['Open'].shift(1)) / 2) > self.data['Close']) and \
        (self.data['Open'] > self.data['Close']) and (self.data['Open'] > self.data['Close'].shift(1)) and\
        (self.data['Close'] > self.data['Open'].shift(1)) and \
        ((self.data['Open'] - self.data['Close']) / (.001 + (H - L)) > .6))

    def bullish_harami(self):
        """Bullish Harami
        ((O1 > C1) AND (C > O) AND (C <= O1) AND (C1 <= O)
        AND ((C - O) < (O1 - C1)))"""
        return((self.data['Open'].shift(1) > self.data['Close'].shift(1)) and \
        (self.data['Close'] > self.data['Open']) and (self.data['Close'] <= self.data['Open'].shift(1)) and\
        (self.data['Close'].shift(1) <= self.data['Open']) and \
        ((self.data['Close'] - self.data['Open']) < (self.data['Open'].shift(1) - self.data['Close'].shift(1))))

    def bearish_harami(self):
        """Bearish Harami
        ((C1 > O1) AND (O > C) AND (O <= C1) AND (O1 <= C) AND ((O - C) < (C1 - O1)))"""
        return((self.data['clsoe'].shift(1) > self.data['Open'].shift(1)) and \
        (self.data['Open'] > self.data['clsoe']) and \
        (self.data['Open'] <= self.data['clsoe'].shift(1)) and\
        (self.data['Open'].shift(1) <= self.data['clsoe']) and \
        ((self.data['Open'] - self.data['clsoe']) < (self.data['clsoe'].shift(1) - self.data['Open'].shift(1))))

    def morning_star(self):
        """Morning Star
        ((O2>C2)AND((O2-C2)/(.001+H2-L2)>.6)AND(C2>O1)AND(O1>C1)AND((H1-L1)>(3*(C1-
        O1)))AND(C>O)AND(O>O1))"""
        return((self.data['Open'].shift(2) > self.data['Close'].shift(2)) and \
        ((self.data['Open'].shift(2) - self.data['Close'].shift(2))/\
        (0.001+self.data['High'].shift(2)-self.data['Low'].shift(2))>.6) and\
        (self.data['Close'].shift(2) > self.data['Open'].shift(1)) and \
        (self.data['Open'].shift(1)>self.data['Close'].shift(1)) and \
        ((self.data['High'].shift(1)-self.data['Low'].shift(1))>(3*(C1-O1)))and\
        (self.data['Close']>self.data['Open'])and\
        (self.data['Open']>self.data['Open'].shift(1)))

    def evening_star(self):
        """Evening Star
        ((C2 > O2) AND ((C2 - O2) / (.001 + H2 - L2) > .6) AND
        (C2 < O1) AND (C1 > O1) AND ((H1 - L1) > (3 * (C1 - O1)))
        AND (O > C) AND (O < O1))"""
        return((self.data['Close'].shift(2) > self.data['Open'].shift(2)) and
        ((self.data['Close'].shift(2) - self.data['Open'].shift(2)) / (.001 + self.data['High'].shift(2) - self.data['Low'].shift(2)) > .6) and \
        (self.data['Close'].shift(2) < self.data['Open'].shift(1)) and \
        (self.data['Close'].shift(1) > self.data['Open'].shift(1)) and
        ((self.data['High'].shift(1) - self.data['Low'].shift(1)) > (3 * (self.data['Close'].shift(1) - self.data['Open'].shift(1)))) and\
        (self.data['Open'] > self.data['Close']) and
        (self.data['Open'] < self.data['Open'].shift(1)))

    def bullish_kicker(self):
        """1/10Bullish Kicker
        (O1 > C1) AND (O >= O1) AND (C > O)"""
        return((self.data['Open'].shift(1) > self.data['Close'].shift(1)) and\
        (self.data['Open'] >= self.data['Open'].shift(1)) and \
        (self.data['Close'] > self.data['Open']))

    def bearish_kicker(self):
        """Bearish Kicker
        (O1 < C1) AND (O <= O1) AND (C <= O)"""
        return((self.data['Open'].shift(1) < self.data['Close'].shift(1)) and \
        (self.data['Open'] <= self.data['Open'].shift(1)) and \
        (self.data['Close'] <= self.data['Open']))

    def shooting_star(self):
        """Shooting Star
        (((H - L) > 4 * (O - C)) AND ((H - C) / (.001 + H - L) >= 0.75)
        AND ((H - O) / (.001 + H - L) >= 0.75)))"""
        return(((self.data['High'] - self.data['Low']) > ((self.data['Open'] - self.data['Close'])*4)) and \
        ((self.data['High'].shift(2) - self.data['Close']) / ((.001 + self.data['High'] - self.data['Low']) >= 0.75)) and \
        ((self.data['High'] - self.data['Open']) / ((.001 + self.data['High'] - self.data['Low']) >= 0.75)))

    def inverted_hammer(self):
        """Inverted Hammer
        (((H - L) > 3 * (O - C)) AND ((H - C) / (.001 + H - L) > 0.6)
        AND ((H - O) / (.001 + H - L) > 0.6)))"""
        return(((self.data['High'] - self.data['Low']) > ((self.data['Open'] - self.data['Close'])*3)) and \
        ((self.data['High'] - self.data['Close']) / ((.001 + self.data['High'] - self.data['Low']) > 0.6)) and \
        ((self.data['High'] - self.data['Open']) / ((.001 + self.data['High'] - self.data['Low']) > 0.6)))
    
    def run_all(self):
        
        all_funcs = [i[0] for i in inspect.getmembers(self, predicate=inspect.ismethod)][3:-1]
        print(y)
    
a = CR(name='AAPL.csv')
a.read_csvs()
a.data.head()
