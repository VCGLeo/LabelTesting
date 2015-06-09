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
    minNodeCols = 1
    maxNodeCols = 0
    minEdgeCols = 1                            
    maxEdgeCols = 0                            # Note that the paper states needing a maximum of 6 edge colors
    outputFile = "log"                         # File to write output to
    colFolder = "colFiles/"                         # File to write output to


    # Parse command line options
    try:
        opts, args = getopt.getopt(argv, "hvn:s:x:v:y:e:z:", ["help", "version", "network=", "minSize=", "maxSize=", "minNodeCols=", "maxNodeCols=", "minEdgeCols=", "maxEdgeCols="])
    except getopt.GetoptError:
        print "Incorrect arguments/options."
        printOptions()
        sys.exit(2)

    for opt, arg in opts:

        # Specify network type
        if opt in ['-n', '--network']:
            if arg.lower() in netTypes:
                netType = arg
            else:
                print "Unrecognized network type %s, defaulting to path network" % arg

        # Specify minimum network size in nodes
        elif opt in ['-s', '--minSize']:
            minSize = int(arg)

        # Specify maximum network size in nodes
        elif opt in ['-x', '--maxSize']:
            maxSize = int(arg)

        # Specify number of edge colors
        elif opt in ['-v', '--minNodeCols']:
            edgeCols = int(arg)

        # Specify number of edge colors
        elif opt in ['-y', '--maxNodeCols']:
            edgeCols = int(arg)

        # Specify number of edge colors
        elif opt in ['-e', '--minEdgeCols']:
            edgeCols = int(arg)

        # Specify number of edge colors
        elif opt in ['-z', '--maxEdgeCols']:
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

    if maxNodeCols < minNodeCols:
        maxNodeCols = minNodeCols

    if maxEdgeCols < minEdgeCols:
        maxEdgeCols = minEdgeCols

    if minSize == 0:
        print "Error: no size specified"
        sys.exit(2)

#Start doing stuff

    creator = NetCreator()
    nets = []


    for i in xrange(minSize, maxSize + 1):
        for n in xrange(minNodeCols, maxNodeCols + 1):
            for e in xrange(minEdgeCols, maxEdgeCols + 1):
                suffix = str(i) + "_" + str(n) + "_" + str(e)
                if netType == "path" or netType == "all":
                    nets.append(("path" + suffix, creator.createPath(i, n, e)))
                if netType == "cycle" or netType == "all":
                    nets.append(("cycle" + suffix, creator.createCycle(i, n, e)))
                if netType == "star" or netType == "all":
                    nets.append(("star" + suffix, creator.createStar(i, n, e)))
                if netType == "path-star" or netType == "all":
                    nets.append(("path-star" + suffix, creator.createPathStar(i, n, e)))

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
    print "-n specify a network type: path, cycle, star, path-star, all"
    print "-s minimum number of nodes"
    print "-x maximum number of nodes, specify if range is desired"
    print "-v minimum number of node colors"
    print "-y maximum number of node colors, specify if range is desired"
    print "-e minimum number of edge colors"
    print "-z maximum number of edge colors, specify if range is desired"
    print "Files are generated for all combinations in the minimum-maximum ranges"

# Only execute if not loaded as module!
if __name__ == '__main__':
    run(sys.argv[1:])
