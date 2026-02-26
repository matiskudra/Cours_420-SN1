masse = 5
volume = 10

def densite(masse,volume):
    if masse<=0:
        raise ValueError("La masse doit être positive")
    if volume==0:
        raise ZeroDivisionError("Le volume doit être positif")

    return masse/volume

print(f"La densité de {masse}g par {volume}mL est égal à {densite(masse,volume)}g/mL")