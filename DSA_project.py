import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv


filename = 'SP_500_close_2015.csv'
priceData = pd.read_csv(filename,index_col = 0)


for company in priceData:
	companyData = priceData[company]
	pct_change = companyData[1:]/companyData[:-1]
	#print(pct_change)

percent_change = priceData.pct_change()
#print(percent_change)

correlations = percent_change.corr()
#print(correlations)

#print(correlations.get_value('AAPL','MMM'))

aapl_correlations = correlations.loc[:,'AAPL']
print(aapl_correlations.order(ascending = False))#.iloc[-1])

#print(aapl_correlations.iloc[0])

