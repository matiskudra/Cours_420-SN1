def calcul_pourcentage_cummule_TPs(note_tp1, note_tp2):
    return (10*note_tp1*.2) + (10*note_tp2*.3)

def calcul_pourcentage_cummule_examens(examen_1, examen_2):
    return (examen_1*.2) + (examen_2*.3)







nom_etudiant = (input("Nom de l'utilisateur?"))
note_tp1 = int(input("Note de l'utilisateur au TP1? (sur 10)"))
note_tp2 = int(input("Note de l'utilisateur au TP2? (sur 10)"))
examen_1 = int(input("Note de l'utilisateur à l'examen 1? (sur 100)?"))
examen_2 = int(input("Note de l'utilisateur à l'examen 2? (sur 100)?"))


