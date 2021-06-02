import pyrebase
import tkinter as tk
from tkcalendar import DateEntry
import pandas as pd
import serial #import arduino serial
from datetime import datetime #import datatime
import atexit #exit
import threading
import tkinter.messagebox


config = {
        "apiKey": "AIzaSyA6jK31jECwV_yRqx58Eo8QelRhOY0tdOg",
        "authDomain": "iotbase-7acc0.firebaseapp.com",
        "databaseURL": "https://iotbase-7acc0-default-rtdb.firebaseio.com",
        "projectId": "iotbase-7acc0",
        "storageBucket": "iotbase-7acc0.appspot.com",
        "messagingSenderId": "654462981165",
        "appId": "1:654462981165:web:4dc3efb9652cb1b16054a4",
        "measurementId": "G-69YEJ61D4R"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database() 
user = {
        	"Card":["ccabf816","85cbc38","232fbd2","5203b9"],
            "UserName": ["呂旻翰","周軒民","邱柏瑋","陳品傑"],
        	"Phone":["0900-123-456","0999-123-456","0900-456-789","0999-456-789"]
}

class Threader(threading.Thread):
    def __init__(self, *args, **kwargs):
            threading.Thread.__init__(self, *args, **kwargs)
            self.daemon = True
            self.start()
    def call_user(self):
        timetext=datetime.now().strftime('%H:%M:%S')
        nametext=""
        for num,index in enumerate(user['Card']):
            if(self.card_id==user['Card'][num] ):
                nametext=user['UserName'][num]
                break
        if nametext=="" :
            nametext="找不到用戶"
        tk.messagebox.showinfo(title='讀卡成功', message=timetext+' '+nametext)

    def run(self):
        com = '5'
        serialArduino = serial.Serial('com'+com, 115200)

        def doAtExit():
            serialArduino.close() #close arduino serial
            print("Close serial")
            print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))

        atexit.register(doAtExit)#程序退出時，回調函數

        print("serialArduino.isOpen() = " + str(serialArduino.isOpen()))
        i=0
            
        while True:
            while (serialArduino.inWaiting()==0):
                pass
            data_raw = serialArduino.readline(500)

            valueRead = data_raw.decode()    
            date_time = datetime.now().strftime('%Y-%m-%d') #catch local date
            date_time1 = datetime.now().strftime('%H:%M:%S') #catch local time
            print(type(valueRead))
            print("UID:"+valueRead.rstrip())
            print("Date:"+date_time)
            print("Time:"+date_time1)
            self.card_id=valueRead.rstrip()
            
            db = firebase.database()
            db.child("python_final/"+date_time+'/'+str(i)).update({"time":date_time1,"card":valueRead.rstrip()})
            i=i+1
            self.call_user()



class SearchPage(object):
    def bf_goCheck(self):
        self.window.destroy()
        MenuPage()
    def search_user(self):
        date_time=str(self.date_entry.get_date())
        user_data=db.child("python_final/"+date_time).get()
        data=user_data.val()
        #print(self.user_List.size())
        if self.user_List.size()!=0:
            self.user_List.delete(0,tk.END)
        #print(data)     
        if(data != None):     
            for i in range(len(data)):
                #print(data[i])
                text=data[i]['time']+"  "
                for num,index in enumerate(user['Card']):
                    if(data[i]['card']==index):
                        #print(user['UserName'][num],index)
                        text+=user['UserName'][num]
                        break
                #print(text)
                self.user_List.insert("end",text)
    
    def __init__(self):
        #frame
        self.window = tk.Tk()
        self.window.title('搜尋')
        self.window.geometry('400x800')
        self.window.configure(background='white')
        
        def call_user(event):
            self.root=tk.Tk()
            self.root.title('緊急撥號')
            self.root.geometry('200x100')
            name=self.user_List.get(self.user_List.curselection()).split('  ')[1]
            self.check_label=tk.Label(self.root,text='確認撥給'+name+"  請輸入密碼")
            self.check_label.pack()
            
            def pwd_check():
                #print(0)
                if str(self.entry.get())=='123':
                    #print(111)
                    name=self.user_List.get(self.user_List.curselection()).split('  ')[1]
                    #print(name)
                    _show=""
                    for num,index in enumerate(user['UserName']):
                        #print(name+" "+index)
                        #print(_show)
                        if(name==index):
                            _show+=name+"的電話:"+user['Phone'][num]
                            #print(_show)
                            break
                    self.check_label.configure(text=_show)
                    self.entry.destroy()
                    self.button.destroy()
                    tk.Button(self.root,text='退出',command=self.root.destroy).pack()
                else:
                    self.check_label.configure(text="密碼錯誤")
            self.entry=tk.Entry(self.root,font=("Courier", 14, "italic"), background='white')
            self.entry.pack()
            self.button=tk.Button(self.root,text='確認',command=pwd_check)
            self.button.pack()

        #DateEntry
        self.date_entry = DateEntry(self.window, width=18,background='blue', foreground='white', borderwidth=8)
        self.date_entry.pack(padx=10,pady=10)
        #button
        self.search_btn = tk.Button(self.window, text='search',command=self.search_user)
        self.search_btn.pack(padx=5,pady=5)
        self.back_btn = tk.Button(self.window, text='back',command=self.bf_goCheck)
        self.back_btn.pack(padx=5,pady=5)
        #ListBox
        self.list_box=tk.Frame(self.window)
        self.scrollbar=tk.Scrollbar(self.window)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.user_List = tk.Listbox(self.window,width=100)
        self.user_List.pack(side=tk.LEFT,fill=tk.BOTH)
        self.search_user()     
        self.scrollbar.config(command=self.user_List.yview)     
        self.user_List.bind('<Double-Button-1>',call_user)
        self.window.mainloop()



class MenuPage(object):

    def bf_goSearch(self):
        self.windo.destroy()
        SearchPage()
        
    def __init__(self):
        self.windo = tk.Tk()
        self.windo.title('實名制登錄系統')
        self.windo.geometry('400x800')
        self.windo.configure(background='white')
        self.title1=tk.Label(self.windo,text="智慧連網實名制",font = ('Arial', 25),bg = 'white', fg = 'blue')
        self.title1.pack(pady=30)
        self.title2=tk.Label(self.windo,text="悠遊卡登錄系統",font = ('Arial', 25),bg = 'white', fg = 'blue')
        self.title2.pack(pady=30)
        self.title2=tk.Label(self.windo,text="請感應您的卡片",font = ('Arial', 18),bg = 'white')
        self.title2.pack(pady=30)
        tk.Button(self.windo,text="SearchPage", command=self.bf_goSearch).pack()
        self.windo.mainloop()
        


if __name__ == '__main__':
    Threader(name='Thread-name')
    MenuPage()





 



