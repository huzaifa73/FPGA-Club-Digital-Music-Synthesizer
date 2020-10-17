# Importing Tkinter module 
from tkinter import * 
from tkinter.ttk import *
  
# Creating master Tkinter window 
window = Tk() 
window.geometry("600x600") 
window.title("MQP Synth")
window.configure(bg='grey')


# Tkinter string variable 
# able to store any string value 
v = StringVar(window, "1") 
  
# Rendering top label and radio buttons
Label(window, text="Current Selection").grid(row=0)
Radiobutton(window, text="ASDR", variable = v, value="ASDR").grid(row=1)
Radiobutton(window, text="Filter Cuttoff Frequencies", variable = v, value="Filter Cuttoff Frequencies").grid(row=2)
Radiobutton(window, text="Delay Effects", variable = v, value="Delay Effects").grid(row=3)
Radiobutton(window, text="Distortion Effects", variable = v, value="Distortion Effects").grid(row=4, column=3)
Radiobutton(window, text="LFO Amplitude", variable = v, value="LFO Amplitude").grid(row=5, column=2)
Radiobutton(window, text="LFO Control", variable = v, value="LFO Control").grid(row=6)

mainloop()