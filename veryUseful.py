# -*- coding: utf-8 -*-
"""
Names: Akos Furton, ...
DSA Group project

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import csv

##### Read company names into a dictionary
def readNamesIntoDict():
    d = dict()
    input_file = csv.DictReader(open("SP_500_firms.csv"))
    for row in input_file:
        #print(row)
        d[row['Symbol']] = [row['Name'],row['Sector']]
    return d

namesDict = readNamesIntoDict()

compNames = namesDict.keys()

'''
##### Prices into standarad Python data structures

# Read prices into dictionary of lists

def readPricesIntoDict():
    input_file = csv.DictReader(open('SP_500_close_2015.csv', 'r')) 
    d = dict()
    for row in input_file:
        for column, value in row.items():
            d.setdefault(column, []).append(value)
    return d


prices = readPricesIntoDict()

'''
##### Prices into pandas

# Open data with pandas 
filename = 'SP_500_close_2015.csv'
priceData = pd.read_csv(filename,index_col = 0)

print(type(priceData))
print(priceData.columns)

# Get specific data from dataframe

firstPrices =priceData.ix[0] # This is a "series" of first-day prices
print(type(firstPrices))

firstColumnPrices = priceData.ix[:,0] # First company by index 


applePrices = priceData['AAPL'] # Get by column name
msftPrices = priceData['MSFT']

# Create dataframe from series, then add another series
customPrices = applePrices.to_frame('AAPL')
customPrices = customPrices.join(msftPrices.to_frame('MSFT'))

print(customPrices)  

# Normalise data by first price
pricesScaled = priceData.divide(priceData.ix[0]) 
# Plot
priceFig = pricesScaled.plot(legend=False,figsize=(6,4))

# Save figure into working directory
plt.savefig('stocks2015.png', bbox_inches='tight')


# Loop through companies
for index,company in enumerate(priceData.columns):
        print(company,index)


# Turn into numpy matrix
priceMatrix = priceData.as_matrix()
# Into a 1D array
priceArray = priceMatrix.flatten() 

# Numpy is useful for eg math
np.sqrt(200)


