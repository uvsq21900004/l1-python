x = 3
y = 35

if x%y == 0 : 
    print(x, "est divisible par", y)




xA = int(input("donner xA"))
yA = int(input("donner yA"))
A = (xA , yA)
print("A =", A)

xB = int(input("donner xA"))
yB = int(input("donner yB"))
B = (xB , yB)
print("B =",B)

xC = int(input("donner xC"))
yC = int(input("donner yC"))
C = (xC,yC)
print("C =", C)

AB = (((xA-xB)**2)+((yA-yB)**2))**(1/2)
AC = (((xA-xC)**2)+((yA-yC)**2))**(1/2)
print("AB =", AB)
print("AC =", AC)

if AB < AC :
    print("B est le point le plus proche de  A")
else :
    print("C est plus proche de A")



a = 'anticonstitutionnellement'
b = input("donner un caractère")
print(b)

nbroccurance = 0

for i in range(len(a)) :
    if b == a[i] :
        nbroccurance = nbroccurance + 1
print(nbroccurance)