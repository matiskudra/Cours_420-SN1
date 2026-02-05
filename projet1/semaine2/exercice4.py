import random

nombre_mini = int(input("insérer un nombre plus grand que 0"))
nombre_maxi = int(input("insérer un nombre plus grand que le précédent"))
nombre_random = random.randint(nombre_mini, nombre_maxi)
print(f"Nombre le plus bas : {nombre_mini}")
print(f"Nombre le plus haut : {nombre_maxi}")
print()
print(f"Nombre aléatoire généré : {nombre_random}")