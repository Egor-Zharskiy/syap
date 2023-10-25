import pandas as pd

pp = pd.read_csv('price_prepared.csv', delimiter=';', nrows=1000)

print(pp.isnull())
print(pp.isna().sum())
