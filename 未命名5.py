# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:56:14 2021

@author: msn71
"""


from timeit import timeit 
import numpy as np
A = np.random.rand(30,20)
B = np.random.rand(20,30)
def mydot(a,b):
    result = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
if __name__ == '__main__':
    A = np.random.rand(30,20)
    B = np.random.rand(20,30)
    A2=A.tolist()
    B2=B.tolist()
    mydot(A, B)


time1 = timeit(stmt="np.dot(A, B)", setup="import numpy as np;from __main__ import A,B", number=1)
time2 = timeit(stmt='mydot(A2, B2)', setup='import numpy as np; from __main__ import mydot,A2,B2', number=1)

print(time2/time1 > 50)
    