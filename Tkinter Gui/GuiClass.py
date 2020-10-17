'''
This file will contain the definition of the Tkinter class.
'''

import tkinter as tk
import midi_functions as midi
#import radio as r

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MQP Synth")
        self.master.geometry("600x600")
        #self.master.configure(bg='grey')

        #self.rows = 2
        #self.columns = 3
        #self.create_grid(self.master)       #create a grid to put elements in
        
        #self.frames_arr = 
        #self.add_frames_to_each_grid(self.master)

        #self.pack_frame00(master)

        #self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.grid(row=1, column=0) #,sticky=NSEW)

        #self.forget_button = Button(master, text="Delete", command=self.grid_forget)
        #self.forget_button.grid(row=1, column=2)

        #self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.grid(row=1) #,sticky=NSEW)

        #self.radio = Radiobutton(master, text="ASDR", command=self.greet, value=1) #.grid(row=1,column=2)
        #self.radio.grid(row=4) #grid(row=1,column=2)

        #self.radio2 = Radiobutton(master, text="ASDR2", command=self.greet, value=2) #.grid(row=2,column=2)
        #self.radio2.grid(row=0, column=2) #, columnspan=2, rowspan=2, padx=5, pady=5, sticky="ns") 
        
        #self.create_buttons()    # create the buttons for each grid area dynamically 

    def greet(self):
        print("Greetings!")

    def grid_forget(self):
        print("delete sumting")
        #self.radio2.grid_forget()

    def create_grid(self, master):
        #Assuming you want every section to expand equally when you resize the window, I could give all rows and all columns all an identical weight so that extra space is equally divided among the rows and columns:
        self.master.grid_rowconfigure(0, weight=2)
        self.master.grid_rowconfigure(1, weight=3)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

    def create_frames(self, frames_arr):
        print("creating framez")
        #frames_arr[0][0] = 

    def add_frames_to_each_grid(self, master):
        #Add frames to each grid space shown above. These frames can contain multiple GUI widgets. 
        #The naming scheme is self.frame[row][column]
        self.frame00 = tk.Frame(master, bg='grey').grid(row=0, column=0, sticky="nsew")
        self.frame01 = tk.Frame(master, bg='light grey').grid(row=0, column=1, sticky="nsew")
        self.frame02 = tk.Frame(master, bg='grey').grid(row=0, column=2, sticky="nsew")
        self.frame10 = tk.Frame(master, bg='light grey').grid(row=1, column=0, sticky="nsew")
        self.frame11 = tk.Frame(master, bg='grey').grid(row=1, column=1, sticky="nsew")
        self.frame12 = tk.Frame(master, bg='light grey').grid(row=1, column=2, sticky="nsew")

        #tk.Label(self.frame00, text="row0, col0").pack()
        
    def pack_frame00(self, frame):
        print("dog")
        #self.label = tk.Label(self.frame00, text="row0, col0")

    def add_labels_to_each_grid(self, master):
        self.label = tk.Label(master, text="row0, col0")
        self.label.grid(row=0, column=0, sticky="nsew")

        self.label = tk.Label(master, text="row0, col1")
        self.label.grid(row=0, column=1, sticky="nsew")
        
        self.label = tk.Label(master, text="row0, col2")
        self.label.grid(row=0, column=2, sticky="nsew")

        self.label = tk.Label(master, text="row1, col0")
        self.label.grid(row=1, column=0, sticky="nsew")

        self.label = tk.Label(master, text="row1, col1")
        self.label.grid(row=1, column=1, sticky="nsew")

        self.label = tk.Label(master, text="row1, col2")
        self.label.grid(row=1, column=2, sticky="nsew")

    def create_buttons(self):
        print('called create_buttons()')


if __name__ == "__main__":
    print("oink")
    print(midi.x)
    root = tk.Tk()
    my_gui = GUI(root)
    root.mainloop()
#print(midi.x) #< -- how to access all the midi functions in the future. 