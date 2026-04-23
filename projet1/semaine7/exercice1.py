from IPython.core.pylabtools import figsize

temperatures = [
    ("Janvier", 2.5),
    ("Février", 3.0),
    ("Mars", 6.2),
    ("Avril", 10.5),
    ("Mai", 15.3),
    ("Juin", 19.1),
    ("Juillet", 22.4),
    ("Août", 21.9),
    ("Septembre", 17.0),
    ("Octobre", 12.1),
    ("Novembre", 6.8),
    ("Décembre", 3.4)
]
import matplotlib.pyplot as plt
mois = []
valeurs = []

for t in temperatures:
    mois.append(t[0])
    valeurs.append(t[1])
plt.figure(figsize = (14,6))
plt.plot(mois, valeurs, color = "green", marker = "o", markersize = 5)
plt.xlabel("Mois")
plt.ylabel("Température moyenne (°C)")
plt.title("Température moyenne mensuelle dans la réserve naturelle")
plt.grid(
    axis="both",
    linestyle="--",
    linewidth=0.8,
    color="#b0b0b0",
    alpha=0.5
)
plt.show()
