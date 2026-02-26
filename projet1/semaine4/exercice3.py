import math

a = 1
b = 5
c = 6

if (b**2-4*a*c) < 0:
     print("Il n'y a pas de solution réelle pour ces valeurs de a, b et c.")
elif (b**2-4*a*c) == 0:
    print(f"Il y a une seule solution (racine double) : {-b/(2*a)}")
else:
    print(f"Il y a 2 solutions possibles : {(-b + math.sqrt(b**2 - 4*a*c))/2*a} et {(-b - math.sqrt(b**2 - 4*a*c))/2*a}")

