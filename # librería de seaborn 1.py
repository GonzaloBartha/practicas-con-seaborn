# librería de seaborn  

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

propinas = sns.load_dataset("tips")
print(propinas)

sns.displot(propinas["total_bill"], bins=30)
plt.show() #grafico 1

sns.displot(propinas["tip"], bins=30)
plt.show() #grafico 2

sns.jointplot(x="total_bill", y="tip", data=propinas)
plt.show() #grafico 3

sns.jointplot(x="total_bill", y="tip", data=propinas, kind="hex")
plt.show() #grafico 4

sns.jointplot(x="total_bill", y="tip", data=propinas, kind="reg")
plt.show() #grafico 5

sns.jointplot(x="total_bill", y="tip", data=propinas, kind="kde")
plt.show() #grafico 6

sns.pairplot(propinas)
plt.show() #grafico 7

sns.pairplot(propinas, hue="sex")
plt.show() #grafico 8

sns.pairplot(propinas, hue="size")
plt.show() #grafico 9

sns.rugplot(propinas["tip"])
plt.show() #grafico 10

sns.barplot(x="sex", y="total_bill", data=propinas)
plt.show() #grafico 11

sns.countplot(x="sex", data=propinas)
plt.show() #grafico 12

sns.boxplot(x="day", y= "total_bill", data=propinas, palette="Set3")
plt.show() #grafico 13

sns.boxplot(x="day", y= "total_bill", data=propinas, hue="smoker", palette="Set3")
plt.show() #grafico 14

sns.violinplot(x="day",y= "total_bill", data=propinas, hue= "smoker", split=True, palette="Set3")
plt.show() #grafico 15

sns.stripplot(x="day",y= "total_bill", data=propinas, palette="Set3")
plt.show() #grafico 16

sns.stripplot(x="day",y= "total_bill", data=propinas, hue= "sex", palette="Set3")
plt.show() #grafico 17

sns.swarmplot(x="day",y= "total_bill", data=propinas, hue= "sex", palette="Set3")
plt.show() #grafico 17