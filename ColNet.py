###
# @file ColNet.py
# @author Leo van Gansewinkel (l.w.p.h.v.gansewinkel@student.tue.nl)
#
# Class representing a colored node and edge network
###
import collections
import copy

class ColNet:
    def __init__(self):
        self.nodeCols = []          # Array of node colors
        self.edges = []             # Array of edges
        self.edgeCols = []          # Array of edge colors

    # Transforms this ColNet according to the methods described in the paper
    # Note that binary expansion is used and every edge must be represented at least once, so we cannot use 0
    def transform(self):
        # Determine highest number edge colors to be a useful binary encoding
        maxEdgeCol = 0
        for c in self.edgeCols:
            if maxEdgeCol < c:
                maxEdgeCol = c
        maxEdgeCol += 1

        # Determine number of layers
        numLayers = 1
        coverage = 2
        while coverage <= maxEdgeCol:
            coverage *= 2
            numLayers += 1

        # Determine modulo for node colors
        maxNodeCol = 0
        for c in self.nodeCols:
            if maxNodeCol < c:
                maxNodeCol = c
        maxNodeCol += 1

        # Save original edges for later reference
        oldEdges = copy.deepcopy(self.edges)
        self.edges = []

        # Create new nodes and connect layers by edges
        l = 1
        numNodes = len(self.nodeCols)
        while l < numLayers:
            for i in xrange(0, numNodes):
                self.addNode(self.nodeCols[i] + l*maxNodeCol)
                self.edges.append((i + (l-1)*numNodes, i + l*numNodes))
            l += 1 

        # Create new edges
        l = 0
        pl = 1
        numEdges = len(oldEdges)
        while l < numLayers:
            for i in xrange(0, numEdges):
                if (self.edgeCols[i]+1)%(pl*2) >= pl:
                    self.edges.append((oldEdges[i][0] + l*numNodes, oldEdges[i][1] + l*numNodes))
            l += 1 
            pl *= 2 


    def addNode(self, col):
        self.nodeCols.append(col)

    def insertNode(self, col, index):
        self.nodeCols.insert(index, col)

    def addEdge(self, source, target, col):
        self.edgeCols.append(col)
        self.edges.append((source,target))

    #Returns this network in .col format
    def __str__(self):
        nodes = self.nodeCols
        edges = self.edges
        result = "p edge " + str(len(nodes)) + " " + str(len(edges))
        for i in xrange(0, len(nodes)):
            if nodes[i] > 0:
                result +=  "\n v " + str(i + 1) + " " + str(nodes[i])
        for i in xrange(0, len(edges)):
            result +=  "\n e " + str(edges[i][0] + 1) + " " + str(edges[i][1] + 1)

        return result