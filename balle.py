import tkinter as tk

LARGEUR = 600
HAUTEUR = 400

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

def affichage(event) :
    caree1 = canvas.create_rectangle((0,0),(event.x, event.y), fill= "red")
    caree2 = canvas.create_rectangle((event.x,0),(event.y, LARGEUR), fill= "white")
    caree3 = canvas.create_rectangle((0,event.y),(event.x, LARGEUR), fill= "red")
    caree4 = canvas.create_rectangle((event.x,event.y),(LARGEUR, HAUTEUR), fill= "white")


canvas.bind("<Button-1>", affichage )

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]

balle = creer_balle()


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]



def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(30, mouvement)

canvas.bind("<Button-1>", mouvement())


racine.mainloop()

