import pandas as pd
import yfinance as y
import tqdm as tq
import os
from tkinter import *
from tkinter.ttk import *
import time
import datetime as dt
class Update:
    def window(self,file):
        l=len(file)
        c=l//100
        p=0
        
        root = Tk()
        root.title("Update")
        root.geometry("400x100+750+550")
        
        progress = Progressbar(root, orient = HORIZONTAL,length = 300, mode = 'determinate')
        label=Label(root,text="0%")
        progress.pack(padx=10,pady = 10)
        label.pack(padx=10,pady=10)
        
        return (root,progress,label,p,c,l)
    def work(self):
        file="EQUITY_L.csv"
        ob=pd.read_csv(file)
        x=dt.datetime.now()
        root,progress,label,p,c,l=self.window(ob)
     
        for z in tq.trange(1,len(ob)):
              try:
                if z%c==0:
                        progress['value']+=1
                        p+=1
                        label.config(text="{}%".format(p))
                        
                root.update_idletasks()
                time.sleep(1)
                
                i=ob.at[z,"SYMBOL"]
                
                path="/home/soumyadeep/Desktop/Stock Folder/Companies"# TO SAVE IN THE SPECIFIED DIRECTORY. 
                n=path+"/"+i+".csv"
                f=pd.read_csv(n)
                s=str(f["Date"].iloc[-1])[:10]
                
                temp=f.tail(1)
                f.drop(temp.index,inplace=True)
       
                his=y.download(i+".ns",start=s,progress=False)# DOWNLOAD IN DATAFRAME AND CONVERT TO CSV TO AUTOMATICALLY SAVE IT.
                his['Date']=his.index
                res=pd.concat([f,his],ignore_index=True)
                
                res.to_csv(n,index=False)
              except :
                continue
                
        print("SUCCESSFULLY UPDATED\n")

