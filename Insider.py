import pandas as pd
import tqdm as tq
import tabulate as t
from tkinter import *
from tkinter.ttk import *
import time
import display as d

class ins:

    def window(self,file):
        l=len(file)
        c=int(l/100)
        p=0
        
        root = Tk()
        root.title("Insider Bar")
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
             try:
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
                high=[f.at[len(f)-1,"High"],f.at[len(f)-2,"High"]]
                low=[f.at[len(f)-1,"Low"],f.at[len(f)-2,"Low"]]
                
                l.sort()
                lp.sort()
                if f.at[len(f)-1,"Close"]>100 and f.at[len(f)-1,"Volume"]>100000 and l[0]<lp[0] and lp[1]<l[1] and high[0]<high[1] and low[0]>low[1]:
                    ans.append((name,f.at[len(f)-1,"Close"]))
             except (ValueError,KeyError,FileNotFoundError):
                continue                    
        root.destroy()
        u=d.display()
        u.work([["Name","Close"],ans])
        root.destroy() 
        d.work([["Name","Close"],ans])

