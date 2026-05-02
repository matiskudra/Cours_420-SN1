virus = ["Virus-T", "Virus-C", "Virus-G", "Uroboros"]
caracteristiques = [
    "Transforme les humains en zombies et armes biologiques",
    "Provoque des mutations extrêmes et régénère les tissus",
    "Cause des mutations incontrôlables avec régénération cellulaire rapide",
    "Consomme les organismes incompatibles et renforce les hôtes compatibles"
]
virus_et_autres_info = [
    ["Virus-T", 0.9 ,"Transforme les humains en zombies et armes biologiques"],
    ["Virus-C", 0.0001 ,"Provoque des mutations extrêmes et régénère les tissus"],
    ["Virus-G", 0.85, "Cause des mutations incontrôlables avec régénération cellulaire rapide"],
    ["Uroboros", 0.005, "Consomme les organismes incompatibles et renforce les hôtes compatibles"]
]

print(f"Liste des {len(virus)} virus :")
if len(virus) < 1:
    print("Désolé aucun produit pharmaceutique mortel disponible")

for i in range(len(virus)):
    print(f"   {virus_et_autres_info[i][0]} - ", end='')
    if virus_et_autres_info[i][0] == "Virus-C":
        print(f"{virus_et_autres_info[i][2]} (taux de mutation estimé : {virus_et_autres_info[i][1]*100:.2f}%)")
    else:
        print(f"{virus_et_autres_info[i][2]} (taux de mutation estimé : {virus_et_autres_info[i][1]*100:.1f}%")