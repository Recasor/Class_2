from random import *
from tkinter import *

def change_figure():
    global canvas
    canvas.destroy()
    canvas = Canvas(width=z, height=z, bg='white')
    canvas.pack()
    a, b, d, e, f, g = randint(0, z), randint(0, z), randint(0, z), randint(0, z), randint(0, z), randint(0, z)
    x = randint(1, 3)
    if x == 1:
        canvas.create_rectangle(a, b, d, e)
    elif x == 2:
        canvas.create_polygon(a, b, d, e, f, g)
    else:
        canvas.create_oval(a, b, d, e)


z = 300

root = Tk()
root.geometry('500x500')
canvas = Canvas(width=z, height=z, bg='white')
canvas.pack()
btn = Button(root, text='Поменять фигуру', command=change_figure)
btn.pack()
root.mainloop()