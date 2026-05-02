import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mpg_dataset.csv')
df['l_par_100km'] = 235.215/df['mpg']

df.boxplot('l_par_100km', by='origin')
plt.title("Consommation d'essence (L/100km) en fonction de l'origine du véhicule")
plt.ylabel("Consommation d'essence (L/100km)")
plt.xlabel("Origine du véhicule")
plt.suptitle('')
plt.show()