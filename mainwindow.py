import tkinter as t
from PIL import ImageTk, Image
import datetime as dt
import download as d
import High as h
import Low as l
import engulfing as e
import Insider as i
import volumeShokker as v
import update as u
import PlotCompany as pc
import MV as m
class initialize:
        date = dt.datetime.now()
        L=["DOWNLOAD DATA","UPDATE DATA","52 WEEKS HIGH","52 WEEKS LOW","INSIDER","ENGULFING","VOLUME SHOKKER","PLOT DATA"]
        s=["Please select what you wish to do:",f"{date:%A, %B %d, %Y}"]
        obs=[d.dl(),u.Update(),h.high52(),l.low52(),i.ins(),e.engulf(),v.VS(),pc.Plot()]
        def __init__(self):
                self.mw=t.Tk()#parent window
                self.mw.title("MenuWindow")
                self.mw.geometry("1920x1080")#to set window size
                self.mw.configure(bg="green")
                self.img=Image.open("images/pic.png")

        def label_create(self):
                rs=self.img.resize((1920,400))#resize image
                self.img = ImageTk.PhotoImage(rs)# Create an object of tkinter ImageTk
                ilabel = t.Label(self.mw, image =self.img,bg='skyblue')# Create a Label Widget to display the text or Image'''
                tlabel=t.Label(self.mw,text=self.s[0],font=["Arial",20],bg='skyblue')
                #Label to display the Date
                
                dlabel = t.Label(self.mw, text=self.s[1],font=["Arial",30],bg='skyblue')

                ilabel.pack()
                dlabel.pack()
                tlabel.pack(anchor='w')


        '''
        Since a frame is not scrollable,we will create a canvas.
        window=w where w is the widget you want to place onto the canvas.
        (0,0) starting coordinates
        '''
        def button_group(self):
                f=t.Frame(self.mw,height=450,bg='skyblue')
                c=t.Canvas(f,bg='white')
                tf=t.Frame(c)
                scroll=t.Scrollbar(f,orient="vertical",command=c.yview)
                c.create_window((0,0),window=tf,anchor='nw')
                self.button(tf)
                
                tf.update()#to update the height of frame tf
                c.configure(yscrollcommand=scroll.set,scrollregion="0 0 0 %s" % tf.winfo_height())
                c.pack(side='left',padx=5,pady=5)
                scroll.pack(side= 'right',fill='y')
                f.pack(padx=10,pady=10,side=t.LEFT)
                
                mvf=t.Frame(self.mw,height=700,width=700,bg="green")
                mvf.pack(fill=t.BOTH,expand=True)                
                m.MV(mvf)
                               
        '''
        When a PhotoImage object is garbage-collected by Python (e.g. when you return from a function which stored an image in a local variable), 
        the image is cleared even if it’s being displayed by a Tkinter widget.
        To avoid this, the program must keep an extra reference to the image object.
        '''
        def helper(self,s):
                return ImageTk.PhotoImage(Image.open("images/{}".format(s)).resize((50,50)))
        def button(self,tf):
                global p
                p=[self.helper("down.jpg"),self.helper("update.png"),self.helper("high.jpg"),self.helper("low.jpeg"),self.helper("insider.png"),self.helper("engulf.png"),
                self.helper("vol.png"),self.helper("plot.png")]
                for i in range(len(self.L)):
                        b=t.Button(tf,image=p[i],text=self.L[i],width=400,height=60,compound="left",command=self.obs[i].work)
                        b.pack()

ob=initialize()
ob.label_create()
ob.button_group()
ob.mw.mainloop()#to capture any action 

