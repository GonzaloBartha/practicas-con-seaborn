# librería de seaborn 3

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

propinas = sns.load_dataset("tips")
print(propinas.head())

sns.lmplot(x="total_bill", y="tip", data=propinas)
plt.show() #grafico 27

sns.lmplot(x="total_bill", y="tip", data=propinas, hue="sex", markers=["o","v"])
plt.show() #grafico 28 

sns.lmplot(x="total_bill", y="tip", data=propinas, col= "sex")
plt.show() #grafico 29

sns.lmplot(x="total_bill", y="tip", data=propinas, col= "day")
plt.show() #grafico 30

sns.lmplot(x="total_bill", y="tip", data=propinas, col= "day", row="sex")
plt.show() #grafico 31

sns.lmplot(x="total_bill", y="tip", data=propinas, col= "day", hue="sex")
plt.show() #grafico 32

sns.lmplot(x="total_bill", y="tip", hue="sex", data=propinas, aspect=0.8, height=10)
plt.show()#grafico 33

import seaborn as sns
import matplotlib.pyplot as plt

# Cargamos el conjunto de datos
propinas = sns.load_dataset("tips")

# Configuramos el contexto y el estilo
sns.set_context("notebook", font_scale=1.2)
sns.set_style("white")

# Configuramos el tamaño de la figura
plt.figure(figsize=(10, 4))

# Graficamos el countplot con hue para diferenciación de colores
sns.countplot(x="sex", hue="sex", data=propinas, palette=["#3498db", "#e74c3c"], legend=False)

# Eliminamos las espinas izquierda e inferior del gráfico
sns.despine(left=True, bottom=True)

# Mostramos el gráfico
plt.show()