# Importing Tkinter module 
from tkinter import * 
from tkinter.ttk import *

class Window():

    def __init__(self):
        self.master = TK() 
        self.master.geometry("600x600") 
        self.master.title("MQP Synth")
        self.master.configure(bg='grey')
        
        #self.create_grid()
        #top_frame = self.create_top_frame()
        mainloop() 

    def create_grid(self):
        #Assuming you want every section to expand equally when you resize the window, I could give all rows and all columns all an identical weight so that extra space is equally divided among the rows and columns:
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    #def create_top_frame(self):


mainloop()