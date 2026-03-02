#Modifier le code afin de retirer la répétition de code (à l'aide d'une boucle).

import random

def generer_nombre():

    nombre = 0

    unite = 1
    chiffre_aleatoire = random.randint(1,9)
    nombre += chiffre_aleatoire * unite

    unite = 10
    chiffre_aleatoire = random.randint(1,9)
    nombre += chiffre_aleatoire * unite

    unite = 100
    chiffre_aleatoire = random.randint(1,9)
    nombre += chiffre_aleatoire * unite

    return nombre

resultat = generer_nombre()
print(f"Nombre généré : {resultat}")