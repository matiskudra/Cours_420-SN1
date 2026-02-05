montant_ini = float(input("Saisir un montant"))
no_billet_100 = int(montant_ini//100)
montant_restant1 = montant_ini%100
no_billet_50 = int(montant_restant1//50)
montant_restant2 = montant_ini%50
no_billet_20 = int(montant_restant2//20)
montant_restant3 = montant_ini%20
no_billet_10 = int(montant_restant3//10)
montant_restant4 = montant_ini%10
no_billet_5 = int(montant_restant4//5)
montant_restant5 = montant_ini%5
montant_restant5_arrondi = round(montant_restant5, 2)
print()
print(f"Saisir un montant : {montant_ini}")
print("Billets :")
print(f"{no_billet_100} x 100$")
print(f"{no_billet_50} x 50$")
print(f"{no_billet_20} x 20$")
print(f"{no_billet_10} x 10$")
print(f"{no_billet_5} x 5$")
print(f"Reste {montant_restant5_arrondi}$")