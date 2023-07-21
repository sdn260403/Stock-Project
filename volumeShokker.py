import yfinance as y
import pandas as pd
import tabulate as t
from tkinter import *
from tkinter.ttk import *
import time
class VS:
    def window(self,file):
        l=len(file)
        c=int(l/100)
        p=0
        
        root = Tk()
        root.title("VolumeShokker")
        root.geometry("400x100+750+550")
        
        progress = Progressbar(root, orient = HORIZONTAL,length = 300, mode = 'determinate')
        label=Label(root,text="0%")
        progress.pack(padx=10,pady = 10)
        label.pack(padx=10,pady=10)
        
        return (root,progress,label,p,c)
        
    def work(self):
        path="/home/soumyadeep/Desktop/Stock Folder/Companies/"
        file=pd.read_csv('EQUITY_L.csv')
        ans=[]
        
        root,progress,label,p,c=self.window(file)
        
        for i in range(1,len(file)):
        
                if i%c==0:
                        progress['value']+=1
                        p+=1
                        label.config(text="{}%".format(p))
                        
                root.update_idletasks()
                time.sleep(1)
                
                comp=file.at[i,"SYMBOL"]
                name=path+comp+".csv"
                data=pd.read_csv(name)
                ldv=int(data.tail().at[len(data)-1,"Volume"])
                ldc=float(data.tail().at[len(data)-1,"Close"])
                lddc=float(data.tail().at[len(data)-2,"Close"])
                avg=(sum(list(map(float,data.tail(8)["Volume"])))-ldv)/7
                if(ldv>avg and ldv>=100000 and ldc>60.00 and ldc>lddc):
                    ans.append([comp,ldv,avg,ldc])
        root.destroy()  
        print(t.tabulate(ans,headers=["Name","LastDayVolume","AverageVolume","LastDayClose"]))
