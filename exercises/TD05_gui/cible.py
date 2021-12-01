import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
root = tk. Tk()
canvas = tk. Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, background="black")
canvas.grid()
xm , ym = CANVAS_WIDTH/2 , CANVAS_HEIGHT/2

x0,y0=0,0
x1,y1=600,600
n = int(input("donner le nbombre de  cercle a tracer"))


for i in range (0,n):
    Pi=(xm*i)/n,(ym*i)/n
    Q = CANVAS_WIDTH-(xm*i)/n, CANVAS_HEIGHT-(ym*i)/n
    canvas.create_oval(Pi, Q, fill="red")


root.mainloop()