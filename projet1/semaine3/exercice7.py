def aire_rectangle(longeur,largeur):
    return longeur*largeur

print(f"L'aire d'un rectangle de 5 x 3 est : {aire_rectangle(5,3)}") # L'aire d'un rectangle de 5 x 3 est : 15

def volume_prisme(longueur, largeur, hauteur):
    return aire_rectangle(longueur, largeur) * hauteur

print(f"L'aire d'un prisme de 5 x 3 x 4 est : {volume_prisme(5,3, 4)}") # L'aire d'un prisme de 5 x 3 x 4 est : 60