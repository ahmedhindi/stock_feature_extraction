
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick2_ohlc
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


class SdZones:
    def __init__(self, data):
        self.data  = data

    def up_or_down(self):
        """this column will be true if the candle is up """
        self.data['up_down'] = np.where(self.data['Open'] > self.data['Close'], True, False)

    def body(self):
        """the body of the candle"""
        self.data['body'] = (self.data['Close'] - self.data['Open']).abs()

    def spread(self):
        """the spread of the candle"""
        self.data['spread'] = self.data['High'] - self.data['Low']


    def is_exciting_candle(self):
        self.data['is_exciting'] = self.data['body'] > (0.5*self.data['spread'])

    def clean(self):
        """removes unneeded columns"""
        self.data.drop(['up_down', 'body','spread'], axis=1, inplace= True)

    def run_all(self):
        """run all the methods"""
        self.up_or_down()
        self.body()
        self.spread()
        self.is_exciting_candle()
        self.clean()


# In[12]:


fig, ax = plt.subplots(figsize=(32,12))
data = pd.read_csv('data/input/AAPL.csv').tail(50)
data.index = np.arange(data.shape[0])
a = SdZones(data)
a.run_all()
data = a.data
from matplotlib.finance import candlestick2_ohlc
candlestick2_ohlc(ax,data['Open'], data['High'], data['Low'], data['Close'], width=0.6)
plt.vlines(data.index[~data['is_exciting']], data.Close.min(), data.Close.max(), alpha=0.4, colors='r')
plt.vlines(data.index[data['is_exciting']], data.Close.min(), data.Close.max(), alpha=0.4, colors='g')


# In[3]:



data = pd.read_csv('data/input/AAPL.csv')[50:200]
data.index = np.arange(data.shape[0])
sample =  SdZones(data=data)
sample.run_all()
data = sample.data
data['is_2'] = data.is_exciting.shift(1)
data['is_3'] = data.is_exciting < data.is_2


def plot_boring_and_intersting(data):
    data.index = np.arange(data.shape[0])
    fig, ax = plt.subplots(figsize=(32,12))
    candlestick2_ohlc(ax,data['Open'],data['High'],data['Low'],data['Close'],width=0.6)
    plt.vlines(data.index[data['is_exciting']], data.Close.min(), data.Close.max(), alpha=0.2, colors='g')
    plt.vlines(data.index[data['is_3']], data.Close.min(), data.Close.max(), alpha=0.5, colors='b')

plot_boring_and_intersting(data)


# In[4]:


data['ud'] = np.where(data.Close > data.Open,True,False)


# In[5]:


# loop over the dataframe 
#if is_3 == True
    # if the the highs ofter this close did not break this point or all the lows did not break it then mark that point
plot_boring_and_intersting(data)
for ind, i in data.iterrows():
#     print(i[1]['Open'])
    if i['is_3']:
#         print('in')
        if (data.High[ind+1:].max() < i.High):
            plt.hlines(i['Close'], ind,data.index.max(), alpha=0.3, colors='r')
            plt.hlines(i['Open'], ind,data.index.max(), alpha=0.3, colors='r')
        
        elif (data.Low[ind+1:].min() > i.Low):
            plt.hlines(i['Close'], ind,data.index.max(), alpha=0.3, colors='g')
            plt.hlines(i['Open'], ind,data.index.max(), alpha=0.3, colors='g')
#             print(f"index >> {ind}-----,{i.High - data.High[ind:].max()}---,{i.Low - data.Low[ind:].min()}")
        else:
            continue
#             plt.vlines(ind,data.Close.min(), data.Close.max(), alpha=0.5, colors='r')
#             plt.hlines(i['Close'], ind,data.index.max(), alpha=0.3, colors='r')
#             plt.hlines(i['Open'], ind,data.index.max(), alpha=0.3, colors='r')
#               plt.hlines(110, 0,120, colors='r')
            
#             print(ind)
#             print(data.High[ind+1:])
            


# In[6]:


data.is_3.sum()


# In[15]:


"""
if supply and true (high and close)
if supply and true (high and close)


"""


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




