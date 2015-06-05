###
# @file ColNet.py
# @author Leo van Gansewinkel (l.w.p.h.v.gansewinkel@student.tue.nl)
#
# Class representing a colored node and edge network
###
import collections

class ColNet:
    def __init__(self):
        self.nodeCols = []          # Array of node colors
        self.edges = []             # Array of edges
        self.edgeCols = []          # Array of edge colors

    def transform(self):
        pass

    def addNode(self, col):
        self.nodeCols.append(col)

    def insertNode(self, col, index):
        self.nodeCols.insert(index, col)

    def addEdge(self, source, target, col):
        self.edgeCols.append(col)
        self.edgeCols.append((source,target))

    #Returns this network in .col format
    def __str__(self):
        nodes = self.nodeCols
        edges = self.edges
        result = "p edge " + str(len(nodes)) + " " + str(len(edges))
        for i in xrange(1, len(nodes)+1):
            if nodes[i-1] > 0:
                result +=  "\n v " + i + " " + nodes[i-1]
        for i in xrange(1, len(edges)+1):
            result +=  "\n e " + edges[i-1][0] + " " + edges[i-1][1]

        return rep