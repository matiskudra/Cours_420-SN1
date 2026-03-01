import random

chiffre = random.randint(1, 100)
chiffre_utilisateur = -1

while chiffre != chiffre_utilisateur:
    chiffre_utilisateur = int(input("Saisir un chiffre entre 1 et 100"))
    if chiffre > chiffre_utilisateur:
        print("Plus Haut!")
    elif chiffre == chiffre_utilisateur:
        print("Bravo humain, vous avez trouvé le nombre!")
    else:
        print("Plus Bas!")
