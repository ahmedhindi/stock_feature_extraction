class CR:
    def __init__(self, data):
        self.data = data

    def doji(self):
        """Doji
        (O = C)"""
        return(self.data['open'] ==  self.data['colse'])

    def doji_yesterday(self):
        """Doji Yesterday
        (O1 = C1)"""
        return(self.data['open'].shift(1) == self.data['close'].shift(1))

    def doji_and_near_doji(self):
        """Doji and Near Doji
        (ABS(O - C ) <= ((H - L ) * 0.1))"""
        return(((self.data['open'] - self.data['close']).abs()) <= ((self.data['high'] - self.data['low']) * 0.1))

    def bullish_engulfing(self):
        """ Bullish Engulfing
        ((O1 > C1) AND (C > O) AND (C >= O1) AND (C1 >= O) AND ((C - O) > (O1 - C1)))"""
        return((self.data['open'].shift(1) > self.data['close'].shift(1)) and \
        (self.data['close'] > self.data['open']) and \
        (self.data['close'] >= self.data['open'].shift(1)) and \
        (self.data['close'].shift(1) >= self.data['open']) and \
        ((self.data['close']-self.data['open']) > (self.data['open'].shift(1)-self.data['close'].shift(1))))

    def bearish_engulfing(self):
        """Bearish Engulfing
        ((C1 > O1) AND (O > C) AND (O >= C1) AND (O1 >= C) AND ((O - C) > (C1 - O1)))"""
        return((self.data['close'].shift(1) > self.data['open'].shift(1)) and\
        (self.data['open'] > self.data['close']) and \
        (self.data['open'] >= self.data['close'].shift(1)) and \
        (self.data['open'].shift(1) >= self.data['close']) and \
        ((self.data['open']-self.data['close']) > (self.data['close'].shift(1)-self.data['open'].shift(1))))

    def hammer(self):
        """Hammer
        (((H-L)>3*(O-C)AND((C-L)/(.001+H-L)>0.6)AND((O-L)/(.001+H-L)>0.6)))"""
        return(((self.data['high'] - self.data['low']) > ((self.data['open']-self.data['close'])*3)) and \
        ((self.data['close']-self.data['low']) / ((.001+self.data['high']-self.data['low']) > 0.6)) and \
        ((self.data['open'] - self.data['low']) / (.001+self.data['high']-self.data['low']) > 0.6))

    def hanging_man(self):
        """ Hanging Man
        (((H - L) > 4 * (O - C)) AND ((C - L) /
        (.001 + H - L) >= 0.75) AND ((O - L) / (.001 + H - L) >= .075)))"""
        return(((self.data['high'] - self.data['low']) > ((self.data['open'] - self.data['close'])*4)) and \
        ((self.data['close'] - self.data['low']) / ((.001 + self.data['high'] - self.data['low']) >= 0.75)) and\
        ((self.data['open'] - self.data['low']) / ((.001 + self.data['high'] - self.data['low']) >= .075)))


    def pricing_line(self):
        """Piercing Line
        ((C1 < O1) AND (((O1 + C1) / 2) < C) AND (O < C) AND
        (O < C1) AND (C < O1) AND ((C - O) / (.001 + (H - L)) > 0.6))"""
        return(((self.data['close'].shift(1)) < (self.data['open'].shift(1))) and \
        (((self.data['open'].shift(1) + self.data['close'].shift(1)) / 2) < (self.data['close'])) and \
        ((self.data['open'] < self.data['close']) and (self.data['open'] < self.data['close'].shift(1))) and \
        (self.data['close'] < self.data['open'].shift(1)) and \
        ((self.data['close'] - self.data['open']) / (0.001 + (self.data['high'] - self.data['low'])) > 0.6))

    def dark_cloud(self):
        """Dark Cloud
        ((C1 > O1) AND (((C1 + O1) / 2) > C) AND (O > C) AND (O > C1) AND (C > O1)
        AND ((O - C) / (.001 + (H - L)) > .6))"""
        return((self.data['close'].shift(1) > self.data['open'].shift(1)) and \
        (((self.data['close'].shift(1) + self.data['open'].shift(1)) / 2) > self.data['close']) and \
        (self.data['open'] > self.data['close']) and (self.data['open'] > self.data['close'].shift(1)) and\
        (self.data['close'] > self.data['open'].shift(1)) and \
        ((self.data['open'] - self.data['close']) / (.001 + (H - L)) > .6))

    def bullish_harami(self):
        """Bullish Harami
        ((O1 > C1) AND (C > O) AND (C <= O1) AND (C1 <= O)
        AND ((C - O) < (O1 - C1)))"""
        return((self.data['open'].shift(1) > self.data['close'].shift(1)) and \
        (self.data['close'] > self.data['open']) and (self.data['close'] <= self.data['open'].shift(1)) and\
        (self.data['close'].shift(1) <= self.data['open']) and \
        ((self.data['close'] - self.data['open']) < (self.data['open'].shift(1) - self.data['close'].shift(1))))

    def bearish_harami(self):
        """Bearish Harami
        ((C1 > O1) AND (O > C) AND (O <= C1) AND (O1 <= C) AND ((O - C) < (C1 - O1)))"""
        return((self.data['clsoe'].shift(1) > self.data['open'].shift(1)) and \
        (self.data['open'] > self.data['clsoe']) and \
        (self.data['open'] <= self.data['clsoe'].shift(1)) and\
        (self.data['open'].shift(1) <= self.data['clsoe']) and \
        ((self.data['open'] - self.data['clsoe']) < (self.data['clsoe'].shift(1) - self.data['open'].shift(1))))

    def morning_star(self):
        """Morning Star
        ((O2>C2)AND((O2-C2)/(.001+H2-L2)>.6)AND(C2>O1)AND(O1>C1)AND((H1-L1)>(3*(C1-
        O1)))AND(C>O)AND(O>O1))"""
        return((self.data['open'].shift(2) > self.data['close'].shift(2)) and \
        ((self.data['open'].shift(2) - self.data['close'].shift(2))/\
        (0.001+self.data['high'].shift(2)-self.data['low'].shift(2))>.6) and\
        (self.data['close'].shift(2) > self.data['open'].shift(1)) and \
        (self.data['open'].shift(1)>self.data['close'].shift(1)) and \
        ((self.data['high'].shift(1)-self.data['low'].shift(1))>(3*(C1-O1)))and\
        (self.data['close']>self.data['open'])and\
        (self.data['open']>self.data['open'].shift(1)))

    def evening_star(self):
        """Evening Star
        ((C2 > O2) AND ((C2 - O2) / (.001 + H2 - L2) > .6) AND
        (C2 < O1) AND (C1 > O1) AND ((H1 - L1) > (3 * (C1 - O1)))
        AND (O > C) AND (O < O1))"""
        return((self.data['close'].shift(2) > self.data['open'].shift(2)) and
        ((self.data['close'].shift(2) - self.data['open'].shift(2)) / (.001 + self.data['high'].shift(2) - self.data['low'].shift(2)) > .6) and \
        (self.data['close'].shift(2) < self.data['open'].shift(1)) and \
        (self.data['close'].shift(1) > self.data['open'].shift(1)) and
        ((self.data['high'].shift(1) - self.data['low'].shift(1)) > (3 * (self.data['close'].shift(1) - self.data['open'].shift(1)))) and\
        (self.data['open'] > self.data['close']) and
        (self.data['open'] < self.data['open'].shift(1)))

    def bullish_kicker(self):
        """1/10Bullish Kicker
        (O1 > C1) AND (O >= O1) AND (C > O)"""
        return((self.data['open'].shift(1) > self.data['close'].shift(1)) and\
        (self.data['open'] >= self.data['open'].shift(1)) and \
        (self.data['close'] > self.data['open']))

    def bearish_kicker(self):
        """Bearish Kicker
        (O1 < C1) AND (O <= O1) AND (C <= O)"""
        return((self.data['open'].shift(1) < self.data['close'].shift(1)) and \
        (self.data['open'] <= self.data['open'].shift(1)) and \
        (self.data['close'] <= self.data['open']))

    def shooting_star(self):
        """Shooting Star
        (((H - L) > 4 * (O - C)) AND ((H - C) / (.001 + H - L) >= 0.75)
        AND ((H - O) / (.001 + H - L) >= 0.75)))"""
        return(((self.data['high'] - self.data['low']) > ((self.data['open'] - self.data['close'])*4)) and \
        ((self.data['high'].shift(2) - self.data['close']) / ((.001 + self.data['high'] - self.data['low']) >= 0.75)) and \
        ((self.data['high'] - self.data['open']) / ((.001 + self.data['high'] - self.data['low']) >= 0.75)))

    def inverted_hammer(self):
        """Inverted Hammer
        (((H - L) > 3 * (O - C)) AND ((H - C) / (.001 + H - L) > 0.6)
        AND ((H - O) / (.001 + H - L) > 0.6)))"""
        return(((self.data['high'] - self.data['low']) > ((self.data['open'] - self.data['close'])*3)) and \
        ((self.data['high'] - self.data['close']) / ((.001 + self.data['high'] - self.data['low']) > 0.6)) and \
        ((self.data['high'] - self.data['open']) / ((.001 + self.data['high'] - self.data['low']) > 0.6)))
