#Variables contenants les données de 3 échantillons
echantillon1_masse_en_g = 135
echantillon1_volume_cm3 = 84
echantillon2_masse_en_g = 270
echantillon2_volume_cm3 = 151
echantillon3_masse_en_g = 92
echantillon3_volume_cm3 = 113

#Calcul des densitées pour les 3 échantilllons
def calcul(masse_g, volume_cm3):
    return (masse_g/1000)/(volume_cm3/1_000_000)
echantillon1_densite = calcul(echantillon1_masse_en_g, echantillon1_volume_cm3)
echantillon2_densite = calcul(echantillon2_masse_en_g, echantillon2_volume_cm3)
echantillon3_densite = calcul(echantillon3_masse_en_g, echantillon3_volume_cm3)

#Affichage des résultats
print("Densité 1 :", round(echantillon1_densite, 2), "kg/m3")
print("Densité 2 :", round(echantillon2_densite, 2), "kg/m3")
print("Densité 3 :", round(echantillon3_densite, 2), "kg/m3")