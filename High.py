import pandas as pd
import tabulate
from tkinter import *
from tkinter.ttk import *
import time
import display as d
class high52:

    def window(self,file):
        l=len(file)
        c=l//100
        p=0
        
        root = Tk()
        root.title("52WeeksHigh")
        root.geometry("400x100+750+550")
        
        progress = Progressbar(root, orient = HORIZONTAL,length = 300, mode = 'determinate')
        label=Label(root,text="0%")
        progress.pack(padx=10,pady = 10)
        label.pack(padx=10,pady=10)
        
        return (root,progress,label,p,c)
        
    def work(self):
        file=pd.read_csv('EQUITY_L.csv')
        ans=[]
        path="/home/soumyadeep/Desktop/Stock Folder/Companies/"
        
        root,progress,label,p,c=self.window(file)
        
        for ind in range(1,len(file)):
              try:
        
                if ind%c==0:
                        progress['value']+=1
                        p+=1
                        label.config(text="{}%".format(p))
                        
                root.update_idletasks()
                time.sleep(1)
                
                name_new=file.at[ind,"SYMBOL"]+".csv"
                name=path+name_new
                data=pd.read_csv(name)
                temp=data.tail(250)["High"].max()#To Access the last one year data without accessing the whole data
                maxiv=data.tail().at[len(data)-1,"High"]#loc was giving index error
                if temp==maxiv:
                    ans.append([name_new[0:name_new.index('.')],data.tail().at[len(data)-1,'Adj Close'],maxiv])
              except:
                continue
                    
        root.destroy()    
        u=d.display()
        u.work([["Name","Close"],ans])
        root.destroy() 
        d.work([["Name","Close"],ans])
