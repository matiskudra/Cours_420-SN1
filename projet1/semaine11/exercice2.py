import pandas as pd

df = pd.read_csv('tips_dataset.csv')

df['tip_par_personne'] = df['tip']/df['size']
print(df.head(5))

#Étape 2
import matplotlib.pyplot as plt

df['tip_par_personne'].plot(kind='hist', bins=20)
plt.title('Distribution du pourboire par personne')
plt.ylabel('Fréquence')
plt.xlabel('Pourboire par personne')
plt.grid(True)

df.boxplot(column='tip_par_personne', by='size')
plt.title('Pourboire par personne en fonction de la taille du groupe')
plt.ylabel('Pourboire par personne')
plt.xlabel('Taille du groupe')
plt.grid(True)
plt.show()
