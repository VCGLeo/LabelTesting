###
# @file NetCreator.py
# @author Leo van Gansewinkel (l.w.p.h.v.gansewinkel@student.tue.nl)
#
# Creator colored node and edge network for path shaped queries
###
from math import sqrt
from ColNet import ColNet

class NetCreator:
    def __init__(self):
        pass

    ###
    # Creates a path shaped colored node and edge network, with the edges pointing in continuous direction
    #
    # @return The ColNet object constructed
    ###
    def createPath(self, size, nodeCols, edgeCols):
        
        net = self.newNet(size, nodeCols)
        
        for i in xrange(0, size - 1):
            net.addEdge(i, i + 1, self.determineColor(i, edgeCols))

        return net

    ###
    # Creates a cycle shaped colored node and edge network, with the edges pointing in continuous direction
    #
    # @return The ColNet object constructed
    ###
    def createCycle(self, size, nodeCols, edgeCols):
        
        net = self.newNet(size, nodeCols)
        
        for i in xrange(0, size - 1):
            net.addEdge(i, i + 1, self.determineColor(i, edgeCols))
        net.addEdge(size - 1, 0, self.determineColor(i, edgeCols))

        return net

    ###
    # Creates a star shaped colored node and edge network, with the edges pointing to the center
    #
    # @return The ColNet object constructed
    ###
    def createStar(self, size, nodeCols, edgeCols):
        
        net = self.newNet(size, nodeCols)
        
        for i in xrange(1, size):
            net.addEdge(i, 0, self.determineColor(i, edgeCols))

        return net

    ###
    # Creates a path-star shaped colored node and edge network, with the edges pointing to the center of each node on the path
    #
    # @return The ColNet object constructed
    ###
    def createPathStar(self, size, nodeCols, edgeCols):
        
        net = self.newNet(size, nodeCols)

        root = int(math.sqrt(size))
        
        i = 1
        while i < size:
            if i%root == 0:
                net.addEdge(i - root, i, self.determineColor(i, edgeCols))
            else:
                net.addEdge(i, i - i%root, self.determineColor(i, edgeCols))

        return net

    ###
    # @return The number indicating the determined color
    ###
    def determineColor(self, index, maxCol):
        return index%maxCol

    ###
    # @return A new ColNet with the colored nodes already in place
    ###
    def newNet(self, size, nodeCols):
        net = ColNet()
        for i in xrange(0, size):
            net.addNode(self.determineColor(i, nodeCols))
        return net
