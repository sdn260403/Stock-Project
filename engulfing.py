import pandas as pd
import tqdm as tq
import tabulate as t
from tkinter import *
from tkinter.ttk import *
import time

class engulf:
    def window(self,file):
        l=len(file)
        c=int(l/100)
        p=0
        
        root = Tk()
        root.title("Engulfing")
        root.geometry("400x100+750+550")
        
        progress = Progressbar(root, orient = HORIZONTAL,length = 300, mode = 'determinate')
        label=Label(root,text="0%")
        progress.pack(padx=10,pady = 10)
        label.pack(padx=10,pady=10)
        
        return (root,progress,label,p,c)
        
    def work(self):
        path="/home/soumyadeep/Desktop/Stock Folder/Companies/"
        main=pd.read_csv('EQUITY_L.csv')
        ans=[]
        
        root,progress,label,p,c=self.window(main)
        
        for i in tq.trange(1,len(main)):
            
                if i%c==0:
                        progress['value']+=1
                        p+=1
                        label.config(text="{}%".format(p))
                        
                root.update_idletasks()
                time.sleep(1)
                name=main.at[i,"SYMBOL"]
                f=pd.read_csv(path+name+".csv")
                
                lp=[f.at[len(f)-2,"Open"],f.at[len(f)-2,"Close"]]
                l=[f.at[len(f)-1,"Open"],f.at[len(f)-1,"Close"]]
                diff=l[0]-l[1]
                high=[f.at[len(f)-1,"High"],f.at[len(f)-2,"High"]]
                low=[f.at[len(f)-1,"Low"],f.at[len(f)-2,"Low"]]
                l.sort()
                lp.sort()
                if l[0]>lp[0] and lp[1]>l[1] and l[0]>high[1] and l[0]>low[1]:
                    if diff<0:
                        ans.append([name,"DOWN",f.at[len(f)-1,"Close"]])
                    else:
                        ans.append([name,"UP",f.at[len(f)-1,"Close"]])
        root.destroy()
        print(t.tabulate(ans,headers=["Name","Type","Close"]))   
