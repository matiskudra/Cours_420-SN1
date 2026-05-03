import pandas as pd
from matplotlib.pyplot import grid

df = pd.read_csv('mpg_dataset.csv')
df['l_par_100km'] = 235.215/df['mpg']
df = df.dropna(subset=['l_par_100km', 'horsepower'])
y = df['l_par_100km']
x = df[['horsepower']]

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model = model.fit(x,y)

print("Score R² :", model.score(x, y))
print("Coefficient :", model.coef_[0])
print("Intercept :", model.intercept_)

import matplotlib.pyplot as plt

plt.scatter(x, y, color='blue', alpha=0.5, label='Données réelles')
plt.xlabel('Puissance (horsepower) en chevaux')
plt.ylabel("Consommation d'essence (L/100km)")
plt.title("Consommation d'essence en fonction de la puissance du véhicule")
y_pred = model.predict(x)
plt.plot(x, y_pred, color='red', label='Régression linéaire')
plt.legend()
plt.grid()
plt.show()