import tkinter as tk
from typing import Collection

racine = tk. Tk()  #création de la fenètre racine
racine.title("mon dessin") #ajout d'un titre

couleur ="blue"


def Cercle():
    canvas.create_oval(50 , 150, 150, 50, fill = couleur)


def Carre():
    canvas.create_rectangle(50, 150, 150, 50, fill = couleur)


def Croix():
    canvas.create_line(50, 150, 150, 50, fill = couleur)
    canvas.create_line(50, 50, 150, 150, fill = couleur)


def ChoisircCouleur():
    global couleur
    couleur = input("Choisir une couleur, soit :\n-white,\n-black,\n-red,\n-green,\n-blue,\n-cyan,\n-yellow")

canvas = tk.Canvas(background="black")
canvas.grid(row=1, column=1, rowspan=3, columnspan=1)

bouton1 = tk.Button (text="choisir une couleur", command= ChoisircCouleur)
bouton1.grid(column=1, row=0)
bouton2 = tk.Button(text="cercle", command=Cercle)
bouton2.grid(column=0, row=1)
bouton3 = tk.Button(text="carré", command=Carre)
bouton3.grid(column=0, row=2)
bouton4 = tk.Button(text="croix", command=Croix)
bouton4.grid(column=0, row=3)

racine.mainloop()