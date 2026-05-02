import random

chiffre = random.randint(1, 100)
chiffre_utilisateur = -1
chiffres_choisis = []
while chiffre != chiffre_utilisateur:
    chiffre_utilisateur = int(input("Saisir un chiffre entre 1 et 100"))
    if chiffre_utilisateur in chiffres_choisis:
        print()
        print("Tu ne sembles pas être le pingouin glissant le plus loin...")
        print("Tu avais déjà essayé cette réponse...")
    chiffres_choisis.append(chiffre_utilisateur)
    if chiffre > chiffre_utilisateur:
        print()
        print("Plus Haut!")
    elif chiffre == chiffre_utilisateur:
        print()
        print("Bravo humain, vous avez trouvé le nombre!")
    else:
        print()
        print("Plus Bas!")
