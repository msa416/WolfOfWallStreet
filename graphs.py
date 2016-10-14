#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
graph implementations

"""

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
    def addEdge(self, src, dest, weight):
        Digraph.addEdge(self, src, dest, weight)
        Digraph.addEdge(self, dest, src, weight)
