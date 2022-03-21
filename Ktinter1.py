from tkinter import *
from tkinter.ttk import *
import tkinter

window = Tk()
window.title("The Anh")

#them label
lbl = tkinter.Label(window,text = "Helo the anh", fg = "red", font =("Arial", 50))
lbl.grid(column = 0, row = 0)

#them textbox
txt  = Entry(window, width = 20)
txt.grid(column = 0, row = 1)

#Ham ban nut botton
def handleButton():
	lbl.configure(text = "Hi, " + txt.get())
	return

#them botton
btn = Button(window, text = "Click" ,command = handleButton )
btn.grid(column = 1, row = 1)

#them combobox
combo = Combobox(window)
combo['value'] = ["Ban1", "Ban2", "Ban3"]
combo.grid(column = 0, row = 2)

def handleCombo():
	lbl.configure(text = "Hi, " + combo.get())
	return

#them botton
btn = Button(window, text = "ComboClick" ,command = handleCombo )
btn.grid(column = 1, row = 2)

window.mainloop()