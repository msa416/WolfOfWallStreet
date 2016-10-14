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


#input = [('a','b',.8),('a','c',.63),('c','d',.95),('b','d',.32),('b','c',.68),('a','d',.05)]
#print(input)

# Sort the correlations between all pairs of stocks in descending order
sortedWeights = mergeSort(correlation_tuples)
print("Sorted Weights", sortedWeights)

# Create the graph as follows:
    # 1. The nodes of the graph are the stocks
    # 2. The edges between them are the correlations
graph = Digraph()
for x in sortedWeights:
	graph.addEdge(x[0],x[1],x[2])
print(graph)

# Create a single node set from each node in the graph
# Initialize a dictionary where each node points to itself
nodePointers = {src:src for src in graph.edges}
# Initialize a dictionary to store the starting nodes
# As a start, every node is labeled as a starting node
nodeStarting = {src:True for src in graph.edges}
# Initialize a dictionary to store the bottom nodes (that point to themselves)
# As a start, every node is labeled as a bottom node
nodeBottom = {src:True for src in graph.edges}

# Define a function to find the bottom node
def findbottom(node):
    source = node
    destination = nodePointers[source]
    while destination != source: # repeat until reaching a node that points to itself
        source = destination
        destination = nodePointers[source]
    return destination

# Define a function that performs set merging
def mergeSets(k):
    counter = 0
    for key in sortedWeights:
        if counter < k:
            if nodePointers[key[0]] == key[0]: # source node points to itself
                if nodeBottom[key[1]]: # destination is the bottom node
                    # merge the sets containing the source and the destination of the edge
                    nodePointers[key[0]] = key[1]
                    nodeBottom[key[0]] = False
                    nodeStarting[key[1]] = False
                else: # destination is not the bottom node
                    # find bottom node
                    bottom = findbottom(key[1])
                    # make the bottom node point to the other node
                    nodePointers[bottom] = key[0]
                    nodeBottom[bottom] = False
    
                print(nodePointers)
                print(nodeBottom)
                print(nodeStarting)
                
            counter += 1

mergeSets(4)

# Define a function to recover the set using bottom and starting nodes
dict = {}
def recoverSets():
    for b_key, b_value in nodeBottom.items(): # loop over the bottom nodes dictionary
        if b_value: # the node is a bottom node
            dict.setdefault(b_key,[]) # add the bottom node as a key to dict
            for s_key, s_value in nodeStarting.items(): # loop over the starting nodes dictionary
                if s_value: # the node is a starting node
                    bottom = findbottom(s_key)
                    # set the current node to be the starting node
                    current_node = s_key
                    while current_node != bottom:
                        # append the current node to the list corresponding to the bottom node in dict
                        dict[b_key].append(current_node)
                        # change current node to be the node the current node is pointing to
                        current_node = nodePointers[current_node]
            # append the bottom node to the list if the list is not empty
            # it means that we have nodes pointing to the bottom node
            if bool(dict[b_key]):
                dict[b_key].append(b_key)
    return list(dict.values())
                
cluster = recoverSets()

