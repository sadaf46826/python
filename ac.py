import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

files ="C:/Users/arshad/Downloads/Min_Max_Seasonal_IMD_2017.csv"

datadf=pd.read_csv(files)

datadf.head()

autocorrelation_lag1 = datadf['OCT-DEC - MAX'].autocorr(lag=1)

#One year lag

print('One year lag',autocorrelation_lag1)

autocorrelation_lag3 = datadf['OCT-DEC - MAX'].autocorr(lag=3)

#Three year lag

print('Three year lag',autocorrelation_lag3)

autocorrelation_lag9 = datadf['OCT-DEC - MAX'].autocorr(lag=9)

#Nine year lag

print('Nine year lag',autocorrelation_lag9)

autocorrelation_lag1 = datadf['JAN-FEB - MIN'].autocorr(lag=1)

#One year lag

print('One year lag',autocorrelation_lag1)

autocorrelation_lag3 = datadf['JAN-FEB - MIN'].autocorr(lag=3)

#Three year lag

print('Three year lag',autocorrelation_lag3)

autocorrelation_lag9 = datadf['JAN-FEB - MIN'].autocorr(lag=9)

#One year lag

print('Nine year lag',autocorrelation_lag9)
