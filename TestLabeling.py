###
# @file TestLabeling.py
# @author Leo van Gansewinkel (l.w.p.h.v.gansewinkel@student.tue.nl)
#
# Test environment for the performance of colored net transformation and Bliss canonical labelling
###
import os, sys, getopt, time
from NetCreator import NetCreator
from ColNet import ColNet

def run(argv):
    # Default variable values
    netTypes = ["path", "cycle", "star", "path-star", "all"]    # Available network types
    netType = "path"                          # Network Type to actually use
    minSize = 0
    maxSize = 0
    edgeCols = 1
    outputFile = None                         # File to write output to
    colFolder = "colFiles/"                         # File to write output to


    # Parse command line options
    try:
        opts, args = getopt.getopt(argv, "hvg:s:o:", ["help", "version", "network=", "maxSize=", "minSize=", "edgeCols="])
    except getopt.GetoptError:
        print "Incorrect arguments/options."
        printOptions()
        sys.exit(2)

    for opt, arg in opts:

        # Specify network type
        if opt in ['-n', '--network']:
            # Make sure it's a recognized strategy
            if arg.lower() in netTypes:
                netType = arg
            else:
                print "Unrecognized network type %s, defaulting to path network" % arg

        # Specify maximum network size in nodes
        elif opt in ['-x', '--maxSize']:
            maxSize = int(arg)

        # Specify minimum network size in nodes
        elif opt in ['-s', '--minSize']:
            minSize = int(arg)

        # Specify number of edge colors
        elif opt in ['-c', '--edgeCols']:
            edgeCols = int(arg)

        # Print help
        elif opt in ["-h", "--help"]:
            printOptions()
            sys.exit(0)

        # Print version info
        elif opt in ["-v", "--version"]:
            print "Who cares :3"
            sys.exit(0)

    if maxSize < minSize:
        maxSize = minSize

    if minSize == 0:
        print "Error: no size specified"
        sys.exit(2)

    testLabeling(netType, minSize, maxSize, edgeCols, outputFile, colFolder)

def testLabeling(netType, minSize, maxSize, edgeCols, outputFile, colFolder):
    creator = NetCreator()
    nets = []

    if netType == "path" or netType == "all":
        for i in xrange(minSize, maxSize + 1):
            e = edgeCols
            if e >= i:
                e = i-1
            nets.append(("path" + str(i) + "_" + str(e), creator.createPath(i, e)))
    elif netType == "cycle" or netType == "all":
        for i in xrange(minSize, maxSize + 1):
            e = edgeCols
            if e > i:
                e = i
            nets.append(("cycle" + str(i) + "_" + str(e), creator.createCycle(i, e)))
    elif netType == "star" or netType == "all":
        for i in xrange(minSize, maxSize + 1):
            e = edgeCols
            if e >= i:
                e = i-1
            nets.append(("star" + str(i) + "_" + str(e), creator.createStar(i, e)))
#    elif netType == "path-star" or netType == "all":
#        for i in xrange(minSize, maxSize + 1):
#            e = edgeCols
#            if e >= i:
#                e = i-1
#            nets.append(("path-star" + str(i) + "_" + str(e), creator.createPathStar(i, e)))

    s = ""
    if not os.path.exists(colFolder):
        os.makedirs(colFolder)
        
    for n in nets:
        s1 = "Transforming " + str(n[0])
        print s1
        n[1].transform()

        s2 = "Outputting " + str(n[0]) + " to .col file"
        print s2
        f = open(colFolder + n[0] + ".col", "w")
        f.write(str(n[1]))
        f.close()

        s3 = "Running Bliss on " + str(n[0])
        print "Running Bliss on " + str(n[0])
        a = time.clock()
        os.system("bliss " + os.path.abspath(colFolder + n[0] + ".col").replace(" ", "\ "))
        b = time.clock()
        d = b-a
        s4 = "Time taken by Bliss: " + str(d)
        print(s4)
        s += s1 + "\n" + s2 + "\n" + s3 + "\n" + s4 + "\n \n"

    if outputFile:
        f = open(outputFile, "w")
        f.write(s)
        f.close()



def printOptions():
    print "Available options:"
    print "check code"

# Only execute if not loaded as module!
if __name__ == '__main__':
    run(sys.argv[1:])
