import pandas as pd
import seaborn as sns

# Cargar un dataset de ejemplo (por ejemplo, "tips" de Seaborn)
df = sns.load_dataset('tips')

# Mostrar las primeras filas del dataset
print(df.head())

# Resumen estadístico de las columnas numéricas
print(df.describe())

prob_smoker = df['smoker'].value_counts(normalize=True)['Yes']
print(f"Probabilidad de que un cliente sea fumador: {prob_smoker:.2f}")


import matplotlib.pyplot as plt
# df['tip'].hist(bins=10)
# plt.title("Distribución de las propinas")
# plt.xlabel("Propina")
# plt.ylabel("Frecuencia")
# plt.show()




# avg_tip_by_day = df.groupby('day')['tip'].mean()
# print(avg_tip_by_day)

# import seaborn as sns
# sns.boxplot(x='day', y='tip', data=df)
# plt.title("Propinas por día")
# plt.show()


print("Media:", df['tip'].mean())
print("Mediana:", df['tip'].median())
print("Moda:", df['tip'].mode()[0])


prob_tip_above_5 = len(df[df['tip'] > 5]) / len(df)
print(f"Probabilidad de que la propina sea mayor a $5: {prob_tip_above_5:.2f}")


def analyze_column(column):
    print(f"Análisis de {column}:")
    print("Media:", df[column].mean())
    print("Mediana:", df[column].median())
    print("Desviación estándar:", df[column].std())
    print()

analyze_column('tip')
analyze_column('total_bill')





