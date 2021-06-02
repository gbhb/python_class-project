# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:24:08 2021

@author: msn71
"""
from keras.applications.vgg16 import VGG16,preprocess_input, decode_predictions
from keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys
import tkinter as tk
import math
from tkinter import filedialog

window = tk.Tk()
window.title('Dogs+vs.+Cat.py')
window.geometry('400x300')
window.configure(background='black')

header_label = tk.Label(window, text='Dogs+vs.+Cat.py')
header_label.pack()
# 載入完成學習的模型VGG16
model = VGG16(weights='imagenet')
# 用來判斷影像的函式

def calculate_bmi_number():
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    results = predict(window.filename, 10)
    for result in results:
        print(result)
        textExample.insert(1.0,'\n')
        textExample.insert(1.0,result)
    
    
def predict(filename, featuresize):
    img = image.load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(preprocess_input(x))
    results = decode_predictions(preds, top=featuresize)[0]
    return results
# 用來顯示影像的函式
def showimg(filename, title, i):
    im = Image.open(filename)
    im_list = np.asarray(im)
    plt.subplot(2, 5, i)
    plt.title(title)
    plt.axis("off")
    plt.imshow(im_list)
# 判斷影像
textExample = tk.Text(window, height=10)
textExample.pack()

calculate_btn = tk.Button(window, text='file', command=calculate_bmi_number)
calculate_btn.pack()


#plt.figure(figsize=(20, 10))
#for i in range(1):
#    showimg(filename, "query", i+1)
#plt.show()

window.mainloop()