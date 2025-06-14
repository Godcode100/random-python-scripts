import _tkinter
from tkinter.constants import *
tk = _tkinter.Tk()
frame = _tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
label = _tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = _tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()
