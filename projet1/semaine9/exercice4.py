liste = [1, 2, 3, 4, 5]

cas1 = [x*5 for x in liste]
print(cas1)

cas2 = [x*2 for x in liste if x%2 == 0]
print(cas2)

cas3 = [f"le carré de {x} est {x**2}" for x in liste]
print(cas3)

cas4 = [x>3 for x in liste]
print(cas4)

cas5 = ["impair" if x%2 != 0 else x for x in liste]
print(cas5)