virus = ["Virus-T", "Virus-C", "Virus-G", "Uroboros", "caca"]

print(f"Liste des {len(virus)} virus :")
if len(virus) < 1:
    print("Désolé aucun produit pharmaceutique mortel disponible")
for element in virus:
    print("   ", end='')
    print(element)