temperatures = [23.5, 25.4, 27.6, 21.9, 26.7, 24.6]

compteur = len(temperatures)
somme = sum(temperatures)
moyenne = somme/compteur
min_temp = min(temperatures)
max_temp = max(temperatures)

print(f"Températures : {temperatures}")
print(f"nb. mesures : {compteur}")
print(f"somme : {round(somme, 1)}")
print(f"moyenne : {round(moyenne, 2)}")
print(f"min : {min_temp}")
print(f"max : {max_temp}")