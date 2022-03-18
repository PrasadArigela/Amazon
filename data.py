#Three lines to make our compiler able to draw:
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv(r"D:\java files\data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show()

