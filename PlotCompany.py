import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.widgets as wid
import tabulate as t
import tkinter as ti
class Plot:
        def update(self,ind):
                self.ax.clear()
                x,o,c,h,l=self.tx[0:50],self.to[ind:ind+50],self.tc[ind:ind+50],self.th[ind:ind+50],self.tl[ind:ind+50]
                self.ax.bar(x, h, bottom=l, color='b',width=0.01)
                self.ax.bar(x,o,bottom=c,color='r',width=0.3)
                self.ax.set_xlabel("Dates")
                self.ax.set_ylabel("Values")
                self.ax.set_title(self.r)  
                plt.draw()     
        def data(self,r):
                self.r=r
                self.win.destroy()
                f="EQUITY_L.csv"
                read=pd.read_csv(f)
                comp_f="/home/soumyadeep/Desktop/Stock Folder/Companies/"+r+".csv"
                comp_read=pd.read_csv(comp_f)
                self.tx=[str(_) for _ in comp_read.index]
                self.to=comp_read['Open']
                self.tc=comp_read['Close']
                self.th=comp_read['High']
                self.tl=comp_read['Low']
                
                x,o,c,h,l=self.tx[:50],self.to[:50],self.tc[:50],self.th[:50],self.tl[:50]
                
                fig,self.ax=plt.subplots(figsize=(30,30))
                self.ax.bar(x, h, bottom=l, color='b',width=0.01)
                self.ax.bar(x,o,bottom=c,color='r',width=0.3)
                self.ax.set_xlabel("Dates")
                self.ax.set_ylabel("Values")
                self.ax.set_title(r)
                
                plt.subplots_adjust(bottom=0.25)
                ax_slider=plt.axes([0.1,0.1,0.8,0.05])
                slider=wid.Slider(ax_slider,"Number of plots",valmin=0,valmax=len(self.tx),valinit=0,valstep=50)
                slider.on_changed(self.update)
                plt.show()

        def work(self):
                self.win=ti.Tk()
                self.win.geometry("400x100+750+550")
                l = ti.Label(self.win,text = "Enter Company Name: ")
                inputtxt = ti.Text(self.win, height = 3,width = 25,bg = "light yellow")
                def text():
                     self.data(inputtxt.get(1.0,ti.END)[:-1].upper())   

                Display = ti.Button(self.win, height = 2,width = 2,text ="Ok",command = text)
 
                l.pack()
                inputtxt.pack()
                Display.pack()
        
                self.win.mainloop()

