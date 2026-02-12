def fonction_lineaire(a, x, b) :
    print("appel de la fonction")
    resultat = a * x + b
    return resultat

x = 5
y = 10
z = 2
r1 = fonction_lineaire(x, z, y) # Attention à l'ordre des paramètres
x = x - 3
r2 = fonction_lineaire(x, y, z)
print(r1, r2)