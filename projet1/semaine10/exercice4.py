somme = 0
counter = 0
with open("temperatures.txt", "r") as f:
    for ligne in f:
        nombre = float(ligne)
        somme += nombre
        counter += 1
moyenne = (somme / counter)
print(moyenne)

with open('moyenne.txt', "w") as f:
    f.write(str(moyenne))