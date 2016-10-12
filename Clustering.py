class Digraph():
    #edges is a dict mapping each node to a dictionary of edges starting from it
    def __init__(self,filename = None):
        self.edges = {}
        self.numEdges = 0
    
    def addNode(self,node):
        # add a vertex to graph (based on key value)       
        self.edges[node] = set()

    def addEdge(self,src,dest,weight):
        # add the (v,w) edge, making sure the two nodes exist
        if not self.hasNode(src): 
            self.addNode(src)
            self.edges[src] = {}
        if not self.hasNode(dest): 
            self.addNode(dest)
            self.edges[dest] = {}
        if not self.hasEdge(src, dest):
            self.numEdges += 1
            self.edges[src][dest] = weight
  
    def childrenOf(self, v):
        # Returns a node's children
        return self.edges[v].items()
        
    def hasNode(self, v):
        return v in self.edges
        
    def hasEdge(self, v, w):
        return w in self.edges[v]

    def listEdges(self):
        ll = []
        for src,values in self.edges.items():
            for dest,weight in values.items():
                ll.append([src,dest,weight])
        return ll
    
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest,weight in self.edges[src].items():
                result = result + src + '->'\
                         + dest + ', length ' + str(weight) + '\n'
        return result[:-1] # omit final newline

class Graph(Digraph):
    """ Undirected graph: two one-way edges for every edge
        """
    def addEdge(self, src, dest,weight):
        Digraph.addEdge(self, src, dest,weight)
        Digraph.addEdge(self, dest, src,weight)

input = [('a','b',.8),('a','c',.63),('c','d',.95),('b','d',.32),('b','c',.68),('a','d',.05)]

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
sortedWeights = mergeSort(input)
print("sortedweights",sortedWeights)

graph = Digraph()
for x in input:
	graph.addEdge(x[0],x[1],x[2])
#print(graph)


nodePointers = {src:src for src in graph.edges}
nodeBottom = {src:True for src in graph.edges}
nodeTop = {src:True for src in graph.edges}


counter = 0

for k in sortedWeights:
	if counter < 2:
		if nodePointers[k[0]] == k[0]:
			nodePointers[k[0]] = k[1]
			nodeBottom[k[0]] = False
			nodeTop[k[1]] = False
			print(nodePointers)
			print(nodeBottom)
			print(nodeTop)
		counter += 1
#Potential implementation of only able to connect bottom chains???
#According to Heikki we get the same answer either way but we should follow his algorighm as closely as possible
#aka instead of connecting b to c, we see that c connects to d which is a bottom node, so connect bottom node b with bottom node d .
#Now have top and bottom of chains. How to connect the two sets?
		







