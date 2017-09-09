import pandas as pd
import numpy as np
import inspect

class CR:
    def __init__(self, name):
        self.name = name
        self.path = 'data/input/'
        self.data = None

    def _read_csvs(self):
        """Reads the data with the indicators as columns (from the output file)"""
        self.data = pd.read_csv(self.path+self.name, index_col=0)

    def _save_data(self):
        """Saves the file in the file strategy"""
        self.data.to_csv('data/c&le/{}'.format(self.name))

    def doji(self):
        """Doji
        (O = C)"""
        self.data['doji'] = (self.data['Open'] ==  self.data['Close'])

    def doji_yesterday(self):
        """Doji Yesterday
        (O1 = C1)"""
        self.data['doji_yesterday'] = (self.data['Open'].shift(1) == self.data['Close'].shift(1))

    def doji_and_near_doji(self):
        """Doji & Near Doji
        (ABS(O - C ) <= ((H - L ) * 0.1))"""
        self.data['doji_and_near_doji'] = (((self.data['Open'] - self.data['Close']).abs()) <= ((self.data['High'] - self.data['Low']) * 0.1))

    def bullish_engulfing(self):
        """ Bullish Engulfing
        ((O1 > C1) & (C > O) & (C >= O1) & (C1 >= O) & ((C - O) > (O1 - C1)))"""
        self.data['bullish_engulfing'] = ((self.data['Open'].shift(1) > self.data['Close'].shift(1)) & \
        (self.data['Close'] > self.data['Open']) & \
        (self.data['Close'] >= self.data['Open'].shift(1)) & \
        (self.data['Close'].shift(1) >= self.data['Open']) & \
        ((self.data['Close']-self.data['Open']) > (self.data['Open'].shift(1)-self.data['Close'].shift(1))))

    def bearish_engulfing(self):
        """Bearish Engulfing
        ((C1 > O1) & (O > C) & (O >= C1) & (O1 >= C) & ((O - C) > (C1 - O1)))"""
        self.data['bearish_engulfing'] = ((self.data['Close'].shift(1) > self.data['Open'].shift(1)) &\
        (self.data['Open'] > self.data['Close']) & \
        (self.data['Open'] >= self.data['Close'].shift(1)) & \
        (self.data['Open'].shift(1) >= self.data['Close']) & \
        ((self.data['Open']-self.data['Close']) > (self.data['Close'].shift(1)-self.data['Open'].shift(1))))

    def hammer(self):
        """Hammer
        (((H-L)>3*(O-C)&((C-L)/(.001+H-L)>0.6)&((O-L)/(.001+H-L)>0.6)))"""
        self.data['hammer'] = (((self.data['High'] - self.data['Low']) > ((self.data['Open']-self.data['Close'])*3)) & \
        ((self.data['Close']-self.data['Low']) / ((.001+self.data['High']-self.data['Low']) > 0.6)) & \
        ((self.data['Open'] - self.data['Low']) / (.001+self.data['High']-self.data['Low']) > 0.6))

    def hanging_man(self):
        """ Hanging Man
        (((H - L) > 4 * (O - C)) & ((C - L) /
        (.001 + H - L) >= 0.75) & ((O - L) / (.001 + H - L) >= .075)))"""
        self.data['hanging_man'] = (((self.data['High'] - self.data['Low']) > ((self.data['Open'] - self.data['Close'])*4)) & \
        ((self.data['Close'] - self.data['Low']) / ((.001 + self.data['High'] - self.data['Low']) >= 0.75)) &\
        ((self.data['Open'] - self.data['Low']) / ((.001 + self.data['High'] - self.data['Low']) >= .075)))

    def pricing_line(self):
        """Piercing Line
        ((C1 < O1) & (((O1 + C1) / 2) < C) & (O < C) &
        (O < C1) & (C < O1) & ((C - O) / (.001 + (H - L)) > 0.6))"""
        self.data['pricing_line'] = (((self.data['Close'].shift(1)) < (self.data['Open'].shift(1))) & \
        (((self.data['Open'].shift(1) + self.data['Close'].shift(1)) / 2) < (self.data['Close'])) & \
        ((self.data['Open'] < self.data['Close']) & (self.data['Open'] < self.data['Close'].shift(1))) & \
        (self.data['Close'] < self.data['Open'].shift(1)) & \
        ((self.data['Close'] - self.data['Open']) / (0.001 + (self.data['High'] - self.data['Low'])) > 0.6))

    def dark_cloud(self):
        """Dark Cloud
        ((C1 > O1) & (((C1 + O1) / 2) > C) & (O > C) & (O > C1) & (C > O1)
        & ((O - C) / (.001 + (H - L)) > .6))"""
        self.data['dark_cloud'] = ((self.data['Close'].shift(1) > self.data['Open'].shift(1)) & \
        (((self.data['Close'].shift(1) + self.data['Open'].shift(1)) / 2) > self.data['Close']) & \
        (self.data['Open'] > self.data['Close']) & (self.data['Open'] > self.data['Close'].shift(1)) &\
        (self.data['Close'] > self.data['Open'].shift(1)) & \
        ((self.data['Open'] - self.data['Close']) / (.001 + (self.data['High'] - self.data['Low'])) > .6))

    def bullish_harami(self):
        """Bullish Harami
        ((O1 > C1) & (C > O) & (C <= O1) & (C1 <= O)
        & ((C - O) < (O1 - C1)))"""
        self.data['bullish_harami'] = ((self.data['Open'].shift(1) > self.data['Close'].shift(1)) & \
        (self.data['Close'] > self.data['Open']) & (self.data['Close'] <= self.data['Open'].shift(1)) &\
        (self.data['Close'].shift(1) <= self.data['Open']) & \
        ((self.data['Close'] - self.data['Open']) < (self.data['Open'].shift(1) - self.data['Close'].shift(1))))

    def bearish_harami(self):
        """Bearish Harami
        ((C1 > O1) & (O > C) & (O <= C1) & (O1 <= C) & ((O - C) < (C1 - O1)))"""
        self.data['bearish_harami'] = ((self.data['Close'].shift(1) > self.data['Open'].shift(1)) & \
        (self.data['Open'] > self.data['Close']) & \
        (self.data['Open'] <= self.data['Close'].shift(1)) &\
        (self.data['Open'].shift(1) <= self.data['Close']) & \
        ((self.data['Open'] - self.data['Close']) < (self.data['Close'].shift(1) - self.data['Open'].shift(1))))

    def morning_star(self):
        """Morning Star
        ((O2>C2)&((O2-C2)/(.001+H2-L2)>.6)&(C2>O1)&(O1>C1)&((H1-L1)>(3*(C1-
        O1)))&(C>O)&(O>O1))"""
        self.data['morning_star'] = ((self.data['Open'].shift(2) > self.data['Close'].shift(2)) & \
        ((self.data['Open'].shift(2) - self.data['Close'].shift(2))/\
        (0.001+self.data['High'].shift(2)-self.data['Low'].shift(2))>.6) &\
        (self.data['Close'].shift(2) > self.data['Open'].shift(1)) & \
        (self.data['Open'].shift(1)>self.data['Close'].shift(1)) & \
        ((self.data['High'].shift(1)-self.data['Low'].shift(1)) > \
        (3*(self.data['Close'].shift(1)-self.data['Open'].shift(1))))&\
        (self.data['Close']>self.data['Open'])&\
        (self.data['Open']>self.data['Open'].shift(1)))

    def evening_star(self):
        """Evening Star
        (
        (C2 > O2) &
        ((C2 - O2) / (.001 + H2 - L2) > .6) &
        (C2 < O1) & (C1 > O1) &
        ((H1 - L1) > (3 * (C1 - O1)))&
        (O > C) & (O < O1)
        )"""
        self.data['evening_star'] = \
        ((self.data['Close'].shift(2) > self.data['Open'].shift(2)) &\
        ((self.data['Close'].shift(2) - self.data['Open'].shift(2)) / (.001 + self.data['High'].shift(2) - self.data['Low'].shift(2)) > .6) & \
        (self.data['Close'].shift(2) < self.data['Open'].shift(1)) & (self.data['Close'].shift(1) > self.data['Open'].shift(1)) & \
        ((self.data['High'].shift(1) - self.data['Low'].shift(1)) > (3 * (self.data['Close'].shift(1) - self.data['Open'].shift(1)))) &\
        (self.data['Open'] > self.data['Close']) & (self.data['Open'] < self.data['Open'].shift(1)))

    def bullish_kicker(self):
        """1/10Bullish Kicker
        (O1 > C1) & (O >= O1) & (C > O)"""
        self.data['bullish_kicker'] = ((self.data['Open'].shift(1) > self.data['Close'].shift(1)) &\
        (self.data['Open'] >= self.data['Open'].shift(1)) & \
        (self.data['Close'] > self.data['Open']))

    def bearish_kicker(self):
        """Bearish Kicker
        (O1 < C1) & (O <= O1) & (C <= O)"""
        self.data['bearish_kicker'] = ((self.data['Open'].shift(1) < self.data['Close'].shift(1)) & \
        (self.data['Open'] <= self.data['Open'].shift(1)) & \
        (self.data['Close'] <= self.data['Open']))

    def shooting_star(self):
        """Shooting Star
        (
        ((H - L) > 4 * (O - C)) &
        ((H - C) / (.001 + H - L) >= 0.75)
        & ((H - O) / (.001 + H - L) >= 0.75))
        )"""
        self.data['shooting_star'] = (((self.data['High'] - self.data['Low']) > ((self.data['Open'] - self.data['Close'])*4)) & \
        ((self.data['High'] - self.data['Close']) / ((.001 + self.data['High'] - self.data['Low']) >= 0.75)) & \
        ((self.data['High'] - self.data['Open']) / ((.001 + self.data['High'] - self.data['Low']) >= 0.75)))

    def inverted_hammer(self):
        """Inverted Hammer
        (((H - L) > 3 * (O - C)) & ((H - C) / (.001 + H - L) > 0.6)
        & ((H - O) / (.001 + H - L) > 0.6)))"""
        self.data['inverted_hammer'] = (((self.data['High'] - self.data['Low']) > ((self.data['Open'] - self.data['Close'])*3)) & \
        ((self.data['High'] - self.data['Close']) / ((.001 + self.data['High'] - self.data['Low']) > 0.6)) & \
        ((self.data['High'] - self.data['Open']) / ((.001 + self.data['High'] - self.data['Low']) > 0.6)))

    def _run_all(self):
        all_funcs = [i[0] for i in inspect.getmembers(self, predicate=inspect.ismethod) if not i[0].startswith('_')]
        for i in all_funcs:
            eval('self.{}()'.format(i))

a = CR(name='AAPL.csv')
a._read_csvs()
a.inverted_hammer()
