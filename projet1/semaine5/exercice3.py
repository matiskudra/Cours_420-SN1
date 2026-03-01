#Les 100 premier chiffres de la séquence fibonacci
premier_chiffre = 1
deuxieme_chiffre = 1

print(premier_chiffre)
print(deuxieme_chiffre)

for n in range(98):
    suivant = premier_chiffre + deuxieme_chiffre
    print(suivant)
    premier_chiffre = deuxieme_chiffre
    deuxieme_chiffre = suivant