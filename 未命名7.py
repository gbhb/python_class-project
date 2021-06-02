# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:16:16 2021

@author: msn71
"""
import os
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping, CSVLogger
import matplotlib.pyplot as plt

# 定義批次大小、類別數、epoch數
batch_size = 128
num_classes = 10
epochs = 20

# 讀取MNIST資料
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(60000, 784).astype('float32')
x_test = x_test.reshape(10000, 784).astype('float32')
x_train /= 255
x_test /= 255
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
# 只顯示MNIST資料裡的10張

for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.title("M_%d" % i)
    plt.axis("off")
    plt.imshow(x_train[i].reshape(28, 28), cmap=None)
    plt.show()