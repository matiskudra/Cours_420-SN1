populations = {
    "Cerfs": [32, 45, 50, 41],
    "Renards": [12, 15, 13, 10],
    "Lapins": [85, 102, 98, 76],
    "Aigles": [5, 7, 6, 5]
}
saisons = ["Printemps", "Été", "Automne", "Hiver"]


print(f"Recensement pour les {len(populations)} espèces :")
print()

moyenne_max = 0
moyenne = []
for c, v in populations.items():
    moyenne = sum(v)/len(v)

    if moyenne > moyenne_max:
        moyenne_max = moyenne
        nom_espece = c
    print(f"{c} : moyenne annuelle = {round(moyenne, 1)} individus")
print()

print(f"Espèce la plus nombreuse : {nom_espece} ({round(moyenne_max, 1)} individus en moyenne)")

#-----------------------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

couleurs = ["blue", "orange", "green", "red"]

plt.plot(saisons, populations["Cerfs"])
plt.plot(saisons, populations["Renards"])
plt.plot(saisons, populations["Lapins"])
plt.plot(saisons, populations["Aigles"])

plt.show()