# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:39:00 2021

@author: msn71
"""
import numpy as np

from scipy import random, linalg, allclose
A = random.randn(4, 4) # 生成持有亂數值的4x4矩陣A
Q,R = linalg.qr(A) # 對矩陣A進行QR分解
allclose(A,np.dot(Q,R))

from scipy import random, linalg, allclose
A = random.randn(4, 4) # 生成持有亂數值的4x4矩陣A
P, L, U = linalg.lu(A) # 對矩陣A進行LU分解
allclose(A, P.dot(L.dot(U)))

from scipy import array, linalg, dot
A = array([[3, -1.2j], [1.2j, 1]]) # 設定正定埃爾米特矩陣A
L = linalg.cholesky(A, lower=True) # 進行丘列斯基分解
allclose(A, dot(L, L.T.conj())) # 確認A == LL*是否成立