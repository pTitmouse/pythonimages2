from graph import *
import tkinter





def rectangle_row(x0, y0, x1, y1, N, dx, clr1, clr2, clr3):
    brushColor(clr1, clr2, clr3)
    Length = x1 - x0
    for i in range(0, N):
        rectangle(x0, y0, x0 + Length, y1)
        x0 += Length + dx


def backboard():
    x1 = 0
    y1 = 250
    x2 = 500
    y2 = 800

    x3 = 0
    y3 = 0
    x4 = 500
    y4 = 500

    brushColor(0, 0, 0)
    rectangle(x1, y1, x2, y2)
    brushColor(100, 100, 100)
    rectangle(x3, y3, x4, y4)


def house():
    x1 = 30
    y1 = 300
    x2 = 300
    y2 = 650

    brushColor(200, 200, 200)
    rectangle(x1, y1, x2, y2)
    rectangle_row(x1 + 20, y2 - 175, x1 + 80, y2 - 50, 3, 25, 139, 69, 19)  # окна снизу
    rectangle_row(x1+20, y1+110, x1+60, y1+40, 5, 10, 34, 213, 33)  # окна сверху
    rectangle_row(x1, y1 + 70, x1 + 10, y1 + 115, 9, 20, 0, 0, 0)  # перила
    rectangle(x1 - 10, y1 + 115, x2 - 10, y1 + 120)  # подоконник
    rectangle(x1 - 10, y1 + 60, x2 - 3, y1 + 80)  # штука на перилах
    penSize(4)
    line(x2 - 10, y1 + 120, 300, y1 + 110)  # бок пола подокнника

def clouds():
    c.create_oval(250, 200, 450, 220, outline="grey", fill="grey", width=5)
    c.create_oval(300, 110, 500, 80, outline="black", fill="black", width=5)
    c.create_oval(260, 200, 100, 300, outline="grey", fill="grey", width=5)
    c.create_oval(300, 230, 500, 300, outline="grey", fill="grey", width=5)
    c.create_oval(250, 140, 80, 80, outline="grey", fill="grey", width=5)

def update():
  moveObjectBy(obj, 5, 0)
  if xCoord(obj) >= 500:
    close()




canvasSize(500, 800)
penColor('black')
c=canvas()
backboard()
house()
clouds()
brushColor(0, 0, 0)
obj = polygon([(10, 300), (30, 280),  (300, 280), (320, 300)])
onTimer(update, 50)
run()
