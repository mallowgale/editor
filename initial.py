from tkinter import *

canvas_width = 900
canvas_height = 600
brush_size = 5
color = "black"
x1,y1 = 0,0

items=[]
n = 0

def getXY(event):
    global x,y
    x = event.x
    y = event.y

def drawLine():

    w.bind("<Button 1>", getLine)

def getLine(event):
    global items
    global  x1, y1
    x1 = event.x
    y1 = event.y
    w.bind("<Button 1>", paintLine)

def paintLine(event):
    global items
    global n, x1, y1
    global color
    x2 = event.x
    y2 = event.y
    n += 1
    items.append(w.create_line(x1, y1, x2, y2,
                               fill=color,
                               width=2,
                               activedash=(10, 7), tags=str(n)))
    w.bind("<Button 1>", getLine)


def drawRect():
    w.bind("<Button 1>", getRect)


def getRect(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    w.bind("<Button 1>", paintRect)


def paintRect(event):
    global items
    global n,x1,y1
    global color
    x2 = event.x
    y2 = event.y
    n += 1
    items.append(w.create_rectangle(x1, y1, x2, y2,
                       outline = color,
                       width=3,activedash=(10, 7),tags=str(n)))
    w.bind("<Button 1>", getRect)

def drawCircle():
    w.bind("<Button 1>", getCircle)

def getCircle(event):
    global x1, y1
    x1 = event.x
    y1 = event.y
    w.bind("<Button 1>", paintCircle)

def paintCircle(event):
    global items
    global n
    global color
    x2 = event.x
    y2 = event.y
    r = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    n += 1
    items.append(w.create_oval(x1-r,y1-r,x1+r,y1+r,
                    outline = color,
                    width = 3,
                    activedash=(10, 7),tags=str(n)))
    w.bind("<Button 1>", getCircle)

def brush_size_change(new_size):
    global brush_size
    brush_size = new_size

def color_change(new_color):
    global color
    color = new_color

root = Tk()
root.title("Drawings")

w = Canvas(root,
            width=canvas_width,
            height=canvas_height)



rectangle_btn = Button(root, text="RECTANGLE", width=10,foreground="black",
                 command = drawRect)
circle_btn = Button(root, text="CIRCLE", width=10,foreground="black",
                 command = drawCircle)
line_btn = Button(root, text="LINE", width=10,foreground="black",
                 command = drawLine)
red_btn = Button(root, text="RED", width=10,foreground="black",
                 command=lambda: color_change("red"))
black_btn = Button(text="BLACK", width=10,
                 command=lambda: color_change("black"))
clear_btn = Button(text="DELETE ALL", width=10,
                 command=lambda: w.delete("all"))


w.grid(row=2,column=0,
       columnspan=7,padx=5,
       pady=5,sticky=E+W+S+N)

w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

circle_btn.grid(row=0,column=0)
rectangle_btn.grid(row=0,column=1)
line_btn.grid(row = 0, column=2)
red_btn.grid(row=0, column=3)
black_btn.grid(row=0, column=4)
clear_btn.grid(row=0, column=5)



root.mainloop()