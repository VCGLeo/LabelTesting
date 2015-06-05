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
    strategies = ["path", "cycle", "star", "star-path"]    # Available strategies
    strategy = "path"                  # Strategy to actually use
    outputFile = None                         # File to write output to


    # Parse command line options
    try:
        opts, args = getopt.getopt(argv, "hvg:s:o:", ["help", "version", "network=", "size=", "output="])
    except getopt.GetoptError:
        print "Incorrect arguments/options."
        printOptions()
        sys.exit(2)

    for opt, arg in opts:

        # Specify network type
        elif opt in ['-n', '--network']:
            # Make sure it's a recognized strategy
            if arg.lower() in netTypes:
                netType = arg
            else:
                print "Unrecognized network type %s, defaulting to path network" % arg

        # Specify game
        if opt in ['-s', '--size']:
            size = arg

        # Specify optional output file
        elif opt in ['-o', '--output']:
            outputFile = arg

        # Print help
        elif opt in ["-h", "--help"]:
            printOptions()
            sys.exit(0)

        # Print version info
        elif opt in ["-v", "--version"]:
            print "Who cares :3"
            sys.exit(0)

    if False:
        print "Error"
        sys.exit(2)

    solveParityGame(pgfile, strategy, outputFile)



def printOptions():
    print "Available options:"
    print "   -g, --game <pgfile>: The file containing a parity game in PGSolver format"

# Only execute if not loaded as module!
if __name__ == '__main__':
    run(sys.argv[1:])
