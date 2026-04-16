temperatures = [23.5, 25.4, 27.6, 21.9, 26.7, 24.6]

compteur = 0
for t in temperatures:
    compteur += 1

somme = 0
for s in temperatures:
    somme += s

moyenne = somme / compteur

min_temp = temperatures[0]
for t in temperatures:
    if t < min_temp:
        min_temp = t
max_temp = temperatures[-1]
for t in temperatures:
    if t > max_temp:
        max_temp = t

print(f"Températures : {temperatures}")
print(f"nb. mesures : {compteur}")
print(f"somme : {round(somme, 1)}")
print(f"moyenne : {round(moyenne, 2)}")
print(f"min : {min_temp}")
print(f"max : {max_temp}")