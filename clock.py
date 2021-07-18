from tkinter import *
from tkinter.ttk import * #import all
from time import strftime
import os 
import sys 

A = str(input(" press enter to continue ==> "))

root = Tk()
root.title('Clock')
#window
# define time in the window
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
# Styling the label
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'black',
            foreground = 'white')
#clock location 
lbl.pack(anchor = 'center')
time()
    
#loop 
mainloop()
