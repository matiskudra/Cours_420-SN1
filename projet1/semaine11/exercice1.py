import pandas as pd

df = pd.read_csv('tips_dataset.csv')

tip_smoker = df.groupby('smoker')['tip'].mean()
print(tip_smoker)

tip_day = df.groupby('day')['tip'].mean()
print(tip_day)

tip_time = df.groupby('time')['tip'].mean()
print(tip_time)

tip_size = df.groupby('size')['tip'].mean()
print(tip_size)