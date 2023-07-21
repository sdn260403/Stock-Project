from tkinter import *
 
class MV:
    def __init__(self,f):
        self.mt="Mission:\nTo educate people about stock market, and maintaining the discipline by following the rules \n, provide resources, and help them implement our strategy for high returns and less risk, consistently. We\nwant to help people to get higher returns out of their investments. Our major mission is to teach them trade with\npassion and patience."
        self.vt="Vision:\nOur vision is to become the most preferred training institute for stock market training, to help clients to get high \n returns on their investments, through a better understanding of the financial market.\n We aim to provide real-time practical exposure to enhance their knowledge on the stock market and help them achieve\nfinancial freedom."
        self.work(f)
        
    def work(self, master):
        subframe = Frame(master, background="DarkOrange2")
        mtxt = Label(subframe, text =self.mt,font=["Arial",18],bg="DarkOrange2")
        mtxt.place(x=5,y=45)
        subframe.pack(expand = True, fill = BOTH)
 
        subframe2 = Frame(master, background="DarkGoldenrod2")
        vtxt = Label(subframe2, text =self.vt,font=["Arial",18],bg="DarkGoldenrod2")
        vtxt.place(x=5,y=45)
        subframe2.pack(expand=True, fill=BOTH)
 

'''
def mission(self):
                xFrame=t.Frame(self.mw,background="green")
                xFrame.pack(expand = True, fill = t.BOTH, side=t.RIGHT)
                subframe = t.Frame(xFrame, background="blue")
                subject = t.Label(subframe, text = "Subject")
                subject.place(relx=0.5, rely=0.5,anchor=t.CENTER)
                
 
                subframe2 = t.Frame(xFrame, background="red")
                message = t.Label(subframe2, text= "Message")
                message.place(relx=0.5, rely=0.5,anchor=t.CENTER)
                
                subframe.pack(padx=5,pady=5)
                subframe2.pack()
                
subframe = t.Frame(self.mw, background="blue")
                subject = t.Label(subframe, text = "Subject")
                subject.place(relx=0.5, rely=0.5,anchor=t.CENTER)
                #subframe.grid(row=0,column=1)
                subframe.pack(expand = True, fill = t.BOTH, anchor='e')
 
                subframe2 = t.Frame(subframe, background="red")
                message = t.Label(subframe2, text= "Message")
                message.place(relx=0.5, rely=0.5,anchor=t.CENTER)
                #subframe2.grid(row=0,column=2)
                subframe2.pack(expand=True, side=t.RIGHT)'''
