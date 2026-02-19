import time

def calcul_intensif():
    '''
    N'essayez VRAIMENT pas de comprendre le code de cette fonction!
    Vous allez être en mesure de le comprendre à partir du cours sur les boucles.
    La seule chose qui est importante de savoir, c'est que cette fonction prend un
    certain temps pour s'exécuter (1 à 2 secondes en moyenne).
    '''
    total = 0
    for i in range(1, 20000000):  # 20 millions d'itérations
        total += i ** 0.5
    return total

tempA = time.monotonic_ns()
calcul_intensif()
tempB = time.monotonic_ns()

mystere = tempB - tempA # Expression intéressante
print(mystere)