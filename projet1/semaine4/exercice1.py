def fonction_ph(ph):
    if ph>7 :
        return "basique"
    elif ph==7 :
        return "neutre"
    elif ph<7 :
        return "acide"

print(f"Une solution avec un Ph de 5 est : {fonction_ph(5)}")
print(f"Une solution avec un Ph de 7 est : {fonction_ph(7)}")
print(f"Une solution avec un Ph de 10 est : {fonction_ph(10)}")