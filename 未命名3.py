import tkinter as tk
import math
from tkinter import filedialog
window = tk.Tk()
window.title('BMI 計算器')
window.geometry('400x300')
window.configure(background='black')

def calculate_bmi_number():
    window.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    result = window.filename
    result_label.configure(text=result)

def status(bmi):
    if bmi < 18.5:
        return '過輕'
    elif bmi >= 18.5 and bmi < 24:
        return '正常'
    elif bmi >= 24 :
        return '過重'

header_label = tk.Label(window, text='BMI 計算器')
header_label.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='身高（cm）')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='體重（kg）')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='馬上計算', command=calculate_bmi_number)
calculate_btn.pack()

window.mainloop()