import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from numpy import log
df = pd.read_csv("C:/Users/arshad/Downloads/sales-of-shampoo-over-a-three-ye.csv")

df.head()
plt.plot(df['Month'], df['Sales of shampoo over a three year period'])
plt.title('sales by month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()

s = df['Sales of shampoo over a three year period']
x = pd.plotting.autocorrelation_plot(s)
x.plot()
plt.show()

df_meanrolling = df['Sales of shampoo over a three year period'].rolling(5).mean()
plt.plot(df_meanrolling)
plt.show()

df_stdrolling = df['Sales of shampoo over a three year period'].rolling(5).std()
plt.plot(df_stdrolling)
plt.show()

res = adfuller(df['Sales of shampoo over a three year period'])
print('Augmented Dickey-Fuller Statistic:%f'%res[0])
print('p-value: %f' % res[0])
