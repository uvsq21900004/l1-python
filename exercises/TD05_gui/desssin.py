import tkinter as tk
from typing import Collection

racine = tk. Tk()  #création de la fenètre racine
racine.title("mon dessin") #ajout d'un titre

bouton1 = tk.Button(text="choisir une couleur")
bouton1.grid(column=1, row=0)
bouton2 = tk.Button(text="cercle")
bouton2.grid(column=0, row=1)
bouton3 = tk.Button(text="carré")
bouton3.grid(column=0, row=2)
bouton4 = tk.Button(text="croix")
bouton4.grid(column=0, row=3)

canvas = tk.Canvas(background="black")
canvas.grid(row=1, column=1, rowspan=3, columnspan=1 )


racine.mainloop()