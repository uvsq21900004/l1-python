import tkinter as tk
from typing import Collection

racine = tk. Tk()  #création de la fenètre racine
racine.title("mon dessin") #ajout d'un titre

def Cercle():
    canvas.create_oval(50 , 150, 150, 50, fill = "green")
    return Cercle

def Carre():
    canvas.create_rectangle(50, 150, 150, 50, fill = 'red')
    return Carre

def Croix():
    canvas.create_line(50, 150, 150, 50, fill = "yellow")
    canvas.create_line(50, 50, 150, 150, fill = "yellow")
    return Croix

canvas = tk.Canvas(background="black")
canvas.grid(row=1, column=1, rowspan=3, columnspan=1)

bouton1 = tk.Button (text="choisir une couleur", )
bouton1.grid(column=1, row=0)
bouton2 = tk.Button(text="cercle", command=Cercle)
bouton2.grid(column=0, row=1)
bouton3 = tk.Button(text="carré", command=Carre)
bouton3.grid(column=0, row=2)
bouton4 = tk.Button(text="croix", command=Croix)
bouton4.grid(column=0, row=3)

racine.mainloop()