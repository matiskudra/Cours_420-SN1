import pandas as pd

df = pd.read_csv("Turing.csv")

df_nombre = len(df)
df_intelligence = df[df['contribution'].str.contains('intelligence')]
nombre_annes = df['year'].value_counts()
annees_3_plus = nombre_annes[nombre_annes >= 3]

print(f"Nombre total de lauréats : {df_nombre}")
print()

print(f"Lauréats avec 'intelligence dans la contribution :")
for index, ligne in df_intelligence.iterrows():
    print(f"     - {ligne['laureate']}")
print()

print("Années avec 3 lauréats ou plus :")
for annee, total in annees_3_plus.items():
    print(f"     - {annee}")