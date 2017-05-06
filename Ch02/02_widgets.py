#!/usr/bin/python3
# widgets.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import * # for Python 2.* it is Tkinter
from tkinter import ttk # ttk is for themed widgets. it is separate module in Python 2.*, so import Ttk should work

root = Tk()

button = ttk.Button(root, text = 'Click Me')
button.pack() # this makes button visible. it is automatically placed on the widget based on the master/slave relation between the object and it's parent

print(button['text'])
button['text'] = 'Press Me'
button.config(text = 'Push Me')
print(button.config())

print(str(button)) # this is underlying indentifier of the button, different from variables name
print(str(root))

ttk.Label(root, text ='Hello, Tkinter!').pack()

# mainloop() add
root.mainloop()
