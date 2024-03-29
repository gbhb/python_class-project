# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:02:52 2021

@author: msn71
"""
import scipy as sp
import numpy as np

# 需要在scipy之外另行import
from scipy.fftpack import fft
import matplotlib.pyplot as plt
# 生成30 Hz訊號與雜訊的合成訊號y
Fs = 500 # 取樣頻率數
T = 1/Fs # 取樣時間
L = 2**14 # 訊號長度(取樣數)
t = sp.arange(L)*T # 時間向量
y = np.sin(2*np.pi*30*t)
+ 5*sp.randn(t.size) # 訊號生成

# 執行FFT
Y = sp.fftpack.fft(y, L)/L
f = (Fs/L)*sp.arange(L/2 + 1) # 取得頻率向量

# 「原本的時序資料」與「FFT頻率解析結果」的繪製
plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.xlabel('時間 [s]')
plt.ylabel('值')
plt.subplot(2, 1, 2)
plt.plot(f, 2*abs(Y[:L/2 + 1]))
plt.xlabel('頻率 [Hz]')
plt.ylabel('|Y(f)|')