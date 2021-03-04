import tkinter as tk
from tkinter import *
"""
HEIGHT = 600
WIDTH = 800


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='blue')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = tk.Label(frame, text='This is label', bg='yellow')
label.pack(side='left')

button = tk.Button(frame, text="Text button", bg='gray')
button.pack(side='left')

entry = tk.Entry(frame, bg='green')
entry.pack(side='left')

root.mainloop()
"""
class App_PRTG:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame,text="HELLO",command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("Hi there, everyone")

root = Tk()
app = App_PRTG(root)
root.mainloop()
root.destroy()
