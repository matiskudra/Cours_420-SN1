import pandas as pd
df = pd.read_csv('mpg_dataset.csv')

df_jap = df[(df['origin'] == 'japan')]
df_jap_accel = df_jap[(df_jap['acceleration'] >= 19.4)]

df_horsepower = df[df['horsepower'] == df['horsepower'].max()]

df_weight_jap = df_jap[df_jap['weight'] > 2500]

print(f"Les modèles japonais ayant une accélération de 19.4 et plus :")
for index, ligne in df_jap_accel.iterrows():
    print(f"     - {ligne['name']}")