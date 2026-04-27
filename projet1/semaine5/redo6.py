def pyramide(hauteur):
    nb_etoiles = 1
    nb_espaces = hauteur - 1
    for i in range(hauteur):
        for j in range(nb_espaces):
            print("  ", end="")
        for k in range(nb_etoiles):
            print("* ", end='')
        nb_etoiles += 2
        nb_espaces -= 1
        print(" ")

pyramide(5)
pyramide(3)
pyramide(7)
