import pandas as pd
df = pd.read_csv('mpg_dataset.csv')

df_jap = df[(df['origin'] == 'japan')]
df_jap_accel = df_jap[(df_jap['acceleration'] >= 19.4)]

df_horsepower_top5 = df.sort_values(['horsepower'], ascending=False).head(5)

df_weight_jap = df_jap[df_jap['weight'] > 2500]

print(f"Les modèles japonais ayant une accélération de 19.4 et plus :")
for index, ligne in df_jap_accel.iterrows():
    print(f"     - {ligne['name']}")
print()

print("Les 5 voitures avec le plus de horsepower :")
for index, ligne in df_horsepower_top5.iterrows():
    print(f"     - {ligne['name']}")
print()

print(f"Le nombre de voitures japonaises avec un poid supérieur à 2500 : {len(df_weight_jap)}")