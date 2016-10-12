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

correlations = correlations.where(np.triu(np.ones(correlations.shape)).astype(np.bool))
correlations = correlations.stack().reset_index()
correlations.columns = ['Company1', 'Company2', 'Correlation']

correlation_tuples = [tuple(x) for x in correlations.values]

# Sort edges in decreasing correlation

def mergeSort(array):
	if len(array) > 1:
		mid = len(array) //2
		left = array[:mid]
		right = array [mid:]
		mergeSort(left)
		mergeSort(right)

		i = 0
		j = 0
		k = 0
		while i < len(left) and j < len(right):
			if left[i][2] > right[j][2]:
				array[k] = left[i]
				i = i + 1
			else:
				array[k] = right[j]
				j = j + 1
			k = k+1
		while i < len(left):
			array[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			array[k] = right[j]
			j += 1
			k += 1
	return(array)

print(mergeSort(correlation_tuples))

class Node:
	def __init__(self, group, inCluster):
		self.group = -1
		self.inCluster = False

	def getGroup(self):
		return self.group

	def setGroup(self,group):
		self.group = group

	def addToCluster(self):
		self.inCluster = True

	def checkCluster(self):
		return self.inCluster

#for x in correlation_tuples:



#Implement Kruskal's clustering algorithm
#def clustering(array, k):







#print(correlations.get_value('AAPL','MMM'))

#aapl_correlations = correlations.loc[:,'AAPL']
#print(aapl_correlations.order(ascending = False))#.iloc[-1])

#print(aapl_correlations.iloc[0])

