import yfinance as y
import pandas as pd
import datetime as dt
import tqdm as tq
from tkinter import *
from tkinter.ttk import *
import time
import os
class dl:
    def work(self):
        os.mkdir("Companies")
        file="EQUITY_L.csv"
        ob=pd.read_csv(file)
        l=len(ob)
        c=l//100
        p=0
        x=dt.datetime.now()
        
        root = Tk()
        root.title("DownloadWindow")
        root.geometry("400x100+750+550")
        
        progress = Progressbar(root, orient = HORIZONTAL,length = 300, mode = 'determinate')
        label=Label(root,text="0%")
        progress.pack(padx=10,pady = 10)
        label.pack(padx=10,pady=10)
        
        for z in tq.trange(1,l):
                if z%c==0:
                        progress['value']+=1
                        p+=1
                        label.config(text="{}%".format(p))
                        
                root.update_idletasks()
                time.sleep(1)
                i=ob.at[z,"SYMBOL"]
               
                path="Companies/"# TO SAVE IN THE SPECIFIED DIRECTORY. 
                n=path+i+".csv"  
                his=y.download(i+".ns",end="{}-{}-{}".format(x.year,x.month,x.day),progress=False)# DOWNLOAD IN DATAFRAME AND CONVERT TO CSV TO AUTOMATICALLY SAVE IT.
                his.to_csv(n)
        label.config(text=["SUCCESSFULLY DOWNLOADED"],font=["Arial",20])
        root.mainloop()

