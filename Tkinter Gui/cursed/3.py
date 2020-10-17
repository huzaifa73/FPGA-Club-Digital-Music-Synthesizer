import Tkinter as tk

def printSumting():
    print("donkey")

root = tk.Tk()

l1 = tk.Label(root, text="hello")
l2 = tk.Label(root, text="world")
f1 = tk.Frame(root)
b1 = tk.Button(f1, text="One button", command=root.quit)
b2 = tk.Button(f1, text="Another button", command=printSumting)
radio2 = tk.Radiobutton(f1, text="ASDR2", command=printSumting)

l1.grid(row=0, column=0)
l2.grid(row=0, column=1)
f1.grid(row=1, column=1, sticky="nsew")

b1.pack(side="top")
b2.pack(side="top")

root.mainloop()