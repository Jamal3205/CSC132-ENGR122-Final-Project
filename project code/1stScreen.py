from tkinter import *
from GUI.py import *
from Time.py import *

window = Tk()
window.title("Pick Set Time or Set Weight")

button_weight = Button(window, text= "Set Weight", width = 30, height = 20, command = lambda : GUI.py)
button_weight.pack(side = LEFT, padx=20, pady=20)

button_time = Button(window, text = "Set Time", width = 30, height = 20, command = lambda : Time.py)
button_time.pack(side = RIGHT, padx = 20, pady = 20)

# start the tkinter event loop
window.mainloop()