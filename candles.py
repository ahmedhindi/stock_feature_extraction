# Doji
# (O = C)
(data['open'] ==  data['colse'])

# Doji Yesterday
# (O1 = C1)
(data['open'].shift(1) == data['close'].shift(1))

# Doji and Near Doji
# (ABS(O - C ) <= ((H - L ) * 0.1))
((data['open'] - data['close']).abs()) <= ((data['high'] - data['low']) * 0.1))

# Bullish Engulfing
# ((O1 > C1) AND (C > O) AND (C >= O1) AND (C1 >= O) AND ((C - O) > (O1 - C1)))
((data['open'].shift(1) > data['close'].shift(1)) and \
(data['close'] > data['open']) and \
(data['close'] >= data['open'].shift(1)) and \
(data['close'].shift(1) >= data['open']) and \
((data['close']-data['open']) > (data['open'].shift(1)-data['close'].shift(1))))

# Bearish Engulfing
# ((C1 > O1) AND (O > C) AND (O >= C1) AND (O1 >= C) AND ((O - C) > (C1 - O1)))
((data['close'].shift(1) > data['open'].shift(1)) and\
(data['open'] > data['close']) and \
(data['open'] >= data['close'].shift(1)) and \
(data['open'].shift(1) >= data['close']) and \
((data['open']-data['close']) > (data['close'].shift(1)-data['open'].shift(1))))

# Hammer
# (((H-L)>3*(O-C)AND((C-L)/(.001+H-L)>0.6)AND((O-L)/(.001+H-L)>0.6)))
(((data['high'] - data['low']) > ((data['open']-data['close'])*3)) and \
((data['close']-data['low']) / ((.001+data['high']-data['low']) > 0.6)) and \
((data['open'] - data['low']) / (.001+data['high']-data['low']) > 0.6))

# Hanging Man
# (((H - L) > 4 * (O - C)) AND ((C - L) /
# (.001 + H - L) >= 0.75) AND ((O - L) / (.001 + H - L) >= .075)))
(((data['high'] - data['low']) > ((data['open'] - data['close'])*4)) and \
((data['close'] - data['low']) / ((.001 + data['high'] - data['low']) >= 0.75)) and\
((data['open'] - data['low']) / ((.001 + data['high'] - data['low']) >= .075)))


# Piercing Line
# ((C1 < O1) AND (((O1 + C1) / 2) < C) AND (O < C) AND
#(O < C1) AND (C < O1) AND ((C - O) / (.001 + (H - L)) > 0.6))
(((data['close'].shift(1)) < (data['open'].shift(1))) and \
(((data['open'].shift(1) + data['close'].shift(1)) / 2) < (data['close'])) and \
((data['open'] < data['close']) and (data['open'] < data['close'].shift(1))) and \
(data['close'] < data['open'].shift(1)) and \
((data['close'] - data['open']) / (0.001 + (data['high'] - data['low'])) > 0.6))

# Dark Cloud
# ((C1 > O1) AND (((C1 + O1) / 2) > C) AND (O > C) AND (O > C1) AND (C > O1)
# AND ((O - C) / (.001 + (H - L)) > .6))
((data['close'].shift(1) > data['open'].shift(1)) and \
(((data['close'].shift(1) + data['open'].shift(1)) / 2) > data['close']) and \
(data['open'] > data['close']) and (data['open'] > data['close'].shift(1)) and\
(data['close'] > data['open'].shift(1)) and \
((data['open'] - data['close']) / (.001 + (H - L)) > .6))

# Bullish Harami
# ((O1 > C1) AND (C > O) AND (C <= O1) AND (C1 <= O)
# AND ((C - O) < (O1 - C1)))
((data['open'].shift(1) > data['close'].shift(1)) and \
(data['close'] > data['open']) and (data['close'] <= data['open'].shift(1)) and\
(data['close'].shift(1) <= data['open']) and \
((data['close'] - data['open']) < (data['open'].shift(1) - data['close'].shift(1))))

# Bearish Harami
# ((C1 > O1) AND (O > C) AND (O <= C1) AND (O1 <= C) AND ((O - C) < (C1 - O1)))
((data['clsoe'].shift(1) > data['open'].shift(1)) and \
(data['open'] > data['clsoe']) and \
(data['open'] <= data['clsoe'].shift(1)) and\
(data['open'].shift(1) <= data['clsoe']) and \
((data['open'] - data['clsoe']) < (data['clsoe'].shift(1) - data['open'].shift(1))))

# Morning Star
# ((O2>C2)AND((O2-C2)/(.001+H2-L2)>.6)AND(C2>O1)AND(O1>C1)AND((H1-L1)>(3*(C1-
# O1)))AND(C>O)AND(O>O1))
((data['open'].shift(2) > data['close'].shift(2)) and \
((data['open'].shift(2) - data['close'].shift(2))/\
(0.001+data['high'].shift(2)-data['low'].shift(2))>.6) and\
(data['close'].shift(2) > data['open'].shift(1)) and \
(data['open'].shift(1)>data['close'].shift(1)) and \
((data['high'].shift(1)-data['low'].shift(1))>(3*(C1-O1)))and\
(data['close']>data['open'])and\
(data['open']>data['open'].shift(1)))

# Evening Star
# ((C2 > O2) AND ((C2 - O2) / (.001 + H2 - L2) > .6) AND
#(C2 < O1) AND (C1 > O1) AND ((H1 - L1) > (3 * (C1 - O1)))
# AND (O > C) AND (O < O1))
((data['close'].shift(2) > data['open'].shift(2)) and
((data['close'].shift(2) - data['open'].shift(2)) / (.001 + data['high'].shift(2) - data['low'].shift(2)) > .6) and \
(data['close'].shift(2) < data['open'].shift(1)) and \
(data['close'].shift(1) > data['open'].shift(1)) and
((data['high'].shift(1) - data['low'].shift(1)) > (3 * (data['close'].shift(1) - data['open'].shift(1)))) and\
(data['open'] > data['close']) and
(data['open'] < data['open'].shift(1)))

# 1/10Bullish Kicker
# (O1 > C1) AND (O >= O1) AND (C > O)
(data['open'].shift(1) > data['close'].shift(1)) and\
(data['open'] >= data['open'].shift(1)) and \
(data['close'] > data['open'])

# Bearish Kicker
# (O1 < C1) AND (O <= O1) AND (C <= O)
(data['open'].shift(1) < data['close'].shift(1)) and \
(data['open'] <= data['open'].shift(1)) and \
(data['close'] <= data['open'])

# Shooting Star
# (((H - L) > 4 * (O - C)) AND ((H - C) / (.001 + H - L) >= 0.75)
# AND ((H - O) / (.001 + H - L) >= 0.75)))
(((data['high'] - data['low']) > ((data['open'] - data['close'])*4)) and \
((data['high'].shift(2) - data['close']) / ((.001 + data['high'] - data['low']) >= 0.75)) and \
((data['high'] - data['open']) / ((.001 + data['high'] - data['low']) >= 0.75)))

# Inverted Hammer
# (((H - L) > 3 * (O - C)) AND ((H - C) / (.001 + H - L) > 0.6)
# AND ((H - O) / (.001 + H - L) > 0.6)))
(((data['high'] - data['low']) > ((data['open'] - data['close'])*3)) and \
((data['high'] - data['close']) / ((.001 + data['high'] - data['low']) > 0.6)) and \
((data['high'] - data['open']) / ((.001 + data['high'] - data['low']) > 0.6)))
