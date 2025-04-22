import pandas as pd
import seaborn as sns

# Cargar un dataset de ejemplo
df = sns.load_dataset('titanic')

print(df.head())

# Supervivencia total:
# ¿Cuántas personas sobrevivieron y cuántas no sobrevivieron?
# Calcula el porcentaje de personas que sobrevivieron.


# Supervivencia por género:
# ¿Cuántos hombres y cuántas mujeres sobrevivieron?
# ¿Cuál es la probabilidad de supervivencia para hombres y mujeres?


# Supervivencia por clase:
# ¿Cuántas personas sobrevivieron en cada clase (pclass)?
# ¿Cuál es la probabilidad de supervivencia por clase?


# Distribución de clases:
# ¿Cuántas personas viajaron en cada clase (pclass)?
# Calcula el porcentaje de pasajeros en cada clase.


# Distribución por género:
# ¿Cuántas personas eran hombres y cuántas eran mujeres?
# Calcula el porcentaje de hombres y mujeres en el barco.


# Distribución de edades:
# ¿Cuántas personas tenían entre 0-10, 10-20, 20-30, 30-40, 40-50, 50-60, y más de 60 años?
# Visualiza la distribución de edades usando un histograma.


# Supervivencia por rango de edad:
# ¿Cuál es la probabilidad de supervivencia para cada rango de edad definido en el ejercicio anterior?


# Edad promedio por género:
# ¿Cuál es la edad promedio de los hombres y las mujeres en el barco?
# ¿Cuál es la edad promedio de los sobrevivientes y de los que no sobrevivieron?


# Edad máxima y mínima:
# ¿Cuál fue la edad máxima y mínima de los pasajeros?
# ¿Quiénes eran las personas más jóvenes y más mayores en el barco?


# Distribución de tarifas (fare):
# ¿Cuál es la tarifa promedio, máxima y mínima pagada por los pasajeros?
# Visualiza la distribución de tarifas usando un histograma.


# Relación entre tarifa y clase:
# ¿Cuál es la tarifa promedio pagada por clase (pclass)?
# Visualiza la relación entre tarifa y clase usando un diagrama de caja.


# Supervivencia por puerto de embarque (embarked):
# ¿Cuál es la probabilidad de supervivencia según el puerto de embarque?
# Visualiza la probabilidad de supervivencia por puerto usando un gráfico de barras.


# Tamaño del grupo familiar (sibsp + parch):
# ¿Cómo afecta el tamaño del grupo familiar la probabilidad de supervivencia?
# Visualiza la relación entre el tamaño del grupo y la probabilidad de supervivencia usando un gráfico de dispersión.


# Relación entre género, clase y supervivencia:
# ¿Cómo afecta el género y la clase la probabilidad de supervivencia?
# Visualiza esta relación usando un gráfico de barras agrupado.


# Análisis de correlación:
# Calcula la correlación entre las columnas numéricas (age, fare, pclass, etc.).
# Visualiza la matriz de correlación usando un mapa de calor.


# Manejo de datos faltantes:
# ¿Cuántos valores faltantes hay en cada columna?
# Elimina las filas con datos faltantes en age y calcula nuevamente las estadísticas.


# Creación de nuevas columnas:
# Crea una columna llamada is_minor que sea True si la edad es menor a 18 años, y False en caso contrario.
# Crea una columna llamada fare_per_person dividiendo la tarifa total (fare) entre el tamaño del grupo (sibsp + parch + 1).







# Sugerencias de gráficos para los ejercicios
# Gráfico de barras:

# Para visualizar supervivencia por género, clase o puerto de embarque.
# Histograma:

# Para analizar la distribución de edades o tarifas.
# Diagrama de caja (boxplot):

# Para comparar tarifas entre clases o edades entre sobrevivientes y no sobrevivientes.
# Gráfico de dispersión:

# Para analizar la relación entre tamaño del grupo familiar y probabilidad de supervivencia.
# Mapa de calor:

# Para visualizar la correlación entre variables numéricas.



