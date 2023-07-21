import pandas as pd
import tqdm as tq
import tabulate as t
class ie:

    def work(self):
        path="/home/soumyadeep/Desktop/Stock Folder/Companies/"
        ans=[]
        main=pd.read_csv("EQUITY_L.csv")
        for i in tq.trange(1,len(main)):
            try:
                name=main.at[i,"SYMBOL"]
                f=pd.read_csv(path+name+".csv")

                o=f.tail(8)["Open"]
                c=f.tail(8)["Close"]
                l=len(f)-1

                flag=0
                for j in range(1,7):
                        if(c.at[l-j-1]<c.at[l-j] or c.at[l-j]>o.at[l-j]):
                                flag=1
                                break
                if not flag:
                        if(o.at[l]<c.at[l-1] and c.at[l]>o.at[l-1]):
                                ans.append(name)
            except:
                continue
        print(t.tabulate(ans,headers=["Name"]))
        
ob=ie()
ob.work()
