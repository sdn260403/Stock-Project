from tkinter import ttk
import tkinter as tk

class display:

      def work(self,data):
        # Creating tkinter window
        window = tk.Tk()
        window.title("RESULT WINDOW")
        window.geometry(("300x200+750+550"))
        
        # Using treeview widget
        treev = ttk.Treeview(window, selectmode ='browse')

        # Constructing vertical scrollbar
        # with treeview
        verscrlbar = ttk.Scrollbar(window,
                                orient ="vertical",
                                command = treev.yview)
        
        # Calling pack method w.r.to vertical
        # scrollbar
        verscrlbar.pack(side ='right', fill ='y')
        
        # Configuring treeview
        treev.configure(xscrollcommand = verscrlbar.set)
        
        # Defining number of columns
        treev["columns"] = tuple(data[0])
        
        # Defining heading
        treev['show'] = 'headings'
        
        # Assigning the width,anchor and heading name to  the
        # respective columns
        for i in range(len(data[0])):
                treev.column(data[0][i], width = 90, anchor ='c')
                treev.heading(data[0][i])
      
        # Inserting the items and their features to the
        # columns built
        for i in range():
                treev.insert("", 'end', text ="",values =data[1][i])
        
        treev.pack(fill='both')
        # Calling mainloop
        window.mainloop()

