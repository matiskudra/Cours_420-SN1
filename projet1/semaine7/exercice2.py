populations = {
    "Cerfs": [32, 45, 50, 41],
    "Renards": [12, 15, 13, 10],
    "Lapins": [85, 102, 98, 76],
    "Aigles": [5, 7, 6, 5]
}
saisons = ["Printemps", "Été", "Automne", "Hiver"]

texte = "moyenne par saison"

print(f"Recensement pour les {len(populations)} espèces :")
print()

moyenne = []
for c, v in populations.items():
    somme = 0
    for n in v:
        somme += n
    moyenne.append(somme / len(v))
    moyenne_instant = somme / len(v)
    print(f"{c} : {texte} = {moyenne_instant}")

