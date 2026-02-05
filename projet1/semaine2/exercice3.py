

pression_matin = int(input("Quelle est la pression du matin?"))
pression_midi = int(input("Quelle est la pression du midi?"))
pression_soir = int(input("Quelle est la pression du soir?"))
list = [pression_matin, pression_midi, pression_soir]
moyenne_pression = sum(list)/len(list)
print("Pression systolique")
print()
print(f"Mesure du matin : {pression_matin}")
print(f"Mesure du midi : {pression_midi}")
print(f"Mesure du soir : {pression_soir}")
print()
print(f"Moyenne de la pression systolique : {moyenne_pression} mmHG")