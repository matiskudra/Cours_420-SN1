def energie_cinetique(masse,vitesse):
    return (masse * (vitesse**2))/2
def force_gravitationelle(masse1,masse2,distance):
    G = 6.674*(10**-11)
    return (G*masse1*masse2)/distance**2