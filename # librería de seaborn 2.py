# librería de seaborn 2 

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

vuelos = sns.load_dataset("flights")
print(vuelos.head(10))

vuelos_matrix = vuelos.pivot_table(index="month", columns="year", values="passengers")
print(vuelos_matrix)

sns.heatmap(vuelos_matrix)
plt.show() #gráfico 19

sns.heatmap(vuelos_matrix, cmap="viridis")   
plt.show() #gráfico 20

sns.heatmap(vuelos_matrix, cmap="coolwarm", linecolor="white", linewidths=2)   
plt.show() #gráfico 21

flores = sns.load_dataset("iris")
print(flores.head(10))

sns.pairplot(flores)
plt.show() #gráfico 22

graficos = sns.PairGrid(flores)
graficos.map(plt.scatter)
plt.show() #gráfico 23

graficos = sns.PairGrid(flores)
graficos.map_diag(sns.histplot)  # Puedes usar histplot o kdeplot
graficos.map_upper(sns.kdeplot)
graficos.map_lower(sns.scatterplot)
plt.show() #gráfico 24


propinas = sns.load_dataset("tips")
print(propinas.head())
print(propinas["time"].unique())
print(propinas["sex"].unique())

grafico2 = sns.FacetGrid(data=propinas, col="time", row="smoker")
grafico2.map(sns.histplot, "total_bill")
plt.show() #gráfico 25
grafico2 = sns.FacetGrid(data=propinas, col="time", row="smoker")
grafico2.map(sns.scatterplot, "total_bill", "tip")  # Usamos sns.scatterplot en lugar de plt.scatterplot
plt.show()