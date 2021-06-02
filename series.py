# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:48:54 2021

@author: msn71
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./^TWII.csv')
plt.figure()
plt.subplot(2, 2, 1)
plt.plot(df['Date'], df['Open'],label = 'Open')
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=90)
plt.legend(loc = 0, prop={'size': "x-large"})


plt.subplot(2, 2, 2)
plt.plot(df['Date'], df['Close'],label = "Close")
plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=90)
plt.legend(loc = 0, prop={'size': "x-large"})


plt.subplot(2, 2, 3)
plt.plot(df['Date'], df['High'],label = "High")

plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=90)
plt.legend(loc = 0, prop={'size': "x-large"})

plt.subplot(2, 2, 4)
plt.plot(df['Date'], df['Low'],label = "Low")

plt.xlabel('Date')
plt.ylabel('Price')
plt.xticks(rotation=90)
plt.legend(loc = 0, prop={'size': "x-large"})

plt.show()




