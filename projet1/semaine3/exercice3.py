def ajoute_cinq(x):
    print("appel de ajoute_cinq")
    return x + 5

def carre(x):
    print("appel de carre")
    return x * x

def calcul_final(a, b):
    print("appel de calcul_final")
    return carre(a) + ajoute_cinq(b)

x = 2
y = 3
resultat = calcul_final(x, y)
print(resultat)