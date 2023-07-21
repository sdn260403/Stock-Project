import pandas as pd
import tabulate as t
from tkinter import *
from tkinter.ttk import *
import time

class low52:

    def window(self,file):
        l=len(file)
        c=int(l/100)
        p=0
        
        root = Tk()
        root.title("52WeeksLow")
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

                if ind%c==0:
                        progress['value']+=1
                        p+=1
                        label.config(text="{}%".format(p))
                        
                root.update_idletasks()
                time.sleep(1)
                
                name_new=file.at[ind,"SYMBOL"]+".csv"
                name=path+name_new
                data=pd.read_csv(name)
                temp=data.tail(250)["Low"].min()#To Access the last one year data without accessing the whole data
                miniv=data.tail().at[len(data)-1,"Low"]#.loc was giving index error
                if temp==miniv:
                    ans.append([name_new[0:name_new.index('.')],data.tail().at[len(data)-1,'Adj Close'],miniv])

        root.destroy()
        print(t.tabulate(ans,headers=['Name','Adj Close','High']))
