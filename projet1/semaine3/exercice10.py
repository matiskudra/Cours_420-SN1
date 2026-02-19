print("Rapport - Résultats des expériences Umbrella Corporation")

print("Échantillon : Virus-T")
print("Température : 37.0°C")
print("pH : 6.2")
print("Mutation Cellulaire : Stable")
print("Contagiosité : Élevée")
print("---------------")

print("Échantillon : Virus-G")
print("Température : 39.5°C")
print("pH : 5.8")
print("Mutation Cellulaire : Instable")
print("Capacité Régénérative : Extrême")
print("---------------")

print("Échantillon : Uroboros")
print("Température : 40.0°C")
print("pH : 7.0")
print("Mutation Cellulaire : Agressive")
print("Compatibilité Hôte : Faible")
print("---------------")

print("Fin du rapport. Données classifiées - Niveau d'accès : Alpha")

#On va améliorer l'exemple ci-haut
print()
def données(echantillion,temp,ph,mutation,variable,separation):
    print(f"Échantillion : {echantillion}")
    print(f"Température : {temp}")
    print(f"pH : {ph}")
    print(f"Mutation Cellulaire : {mutation}")
    print(f"{variable}")
    print(f"{separation}")


print("Rapport - Résultats des expériences Umbrella Corporation")
données("Virus-T","37.0°C",6.2,"Stable","Contagiosité : Élevée", "---------------")
données("Virus-G","39.5°C",5.8,"Instable","Capacité Régénérative : Extrême", "---------------")
données("Uroboros","40.0°C",7.0,"Aggressive","Compatibilité Hôte : Faible", "---------------")
print("Fin du rapport. Données classifiées - Niveau d'accès : Alpha")