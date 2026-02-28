# On définit la fonction avec des paramètres (les entrées)
def calcul_note_finale(tp1, tp2, ex1, ex2):
    # Calcul des moyennes de blocs (sur 100)
    moy_tps = (tp1 * 0.2 + tp2 * 0.3) * 2
    moy_exams = (ex1 * 0.2 + ex2 * 0.3) * 2

    # Calcul de la note globale (somme des points réels)
    note_globale = (tp1 * 0.2 + tp2 * 0.3) + (ex1 * 0.2 + ex2 * 0.3)

    if moy_exams >= 60 and moy_tps >= 60:
        return note_globale
    else:
        # On compare les deux moyennes de blocs selon la consigne
        return min(moy_tps, moy_exams)


# Appel de la fonction avec des valeurs
resultat = calcul_note_finale(70, 70, 70, 70)
print(resultat)