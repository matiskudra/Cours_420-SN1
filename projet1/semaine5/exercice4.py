#Nous allons transformer un code répétitif affichant des lignes d’étoiles sur plusieurs lignes en une version plus propre et flexible grâce à l’utilisation de boucles.

#Ligne #1
print('*', end='')
print()

#Ligne #2
print('*', end='')  # Affiche une étoile et évite le saut de ligne
print('*', end='')
print()             # Génère une ligne vide

#Ligne #3
print('*', end='')
print('*', end='')
print('*', end='')
print()

#Ligne #4
print('*', end='')
print('*', end='')
print('*', end='')
print('*', end='')
print()

nombre_lignes_desire = 4
nombre_lignes_ini = 1

while nombre_lignes_ini <= nombre_lignes_desire:
    nombre_etoiles = 1
    while nombre_etoiles <= nombre_lignes_ini:
        print("*", end='')
        nombre_etoiles += 1
    print()
    nombre_lignes_ini += 1
