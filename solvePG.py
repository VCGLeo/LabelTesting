#!/usr/bin/python
import sys, getopt
from PGSolver.PGSolver import PGSolver

def run(argv):
    # Default variable values
    strategies = ["input-order", "random", "predchain", "predchainp", "predchains", "scc"]    # Available strategies
    pgfile = None                             # File containing the parity game to solve
    strategy = "input-order"                  # Strategy to actually use
    outputFile = None                         # File to write output to


    # Parse command line options
    try:
        opts, args = getopt.getopt(argv, "hvg:s:o:", ["help", "version", "game=", "strategy=", "output="])
    except getopt.GetoptError:
        print "Incorrect arguments/options."
        printOptions()
        sys.exit(2)

    for opt, arg in opts:
        # Specify game
        if opt in ['-g', '--game']:
            pgfile = arg

        # Specify strategy
        elif opt in ['-s', '--strategy']:
            # Make sure it's a recognized strategy
            if arg.lower() in strategies:
                strategy = arg
            else:
                print "Unrecognized strategy %s, defaulting to input order" % arg

        # Specify optional output file
        elif opt in ['-o', '--output']:
            outputFile = arg

        # Print help
        elif opt in ["-h", "--help"]:
            printOptions()
            sys.exit(0)

        # Print version info
        elif opt in ["-v", "--version"]:
            print "0.1"
            sys.exit(0)

    if pgfile == None:
        print "Eror: No pgfile given. Please specify one using the --game option."
        sys.exit(2)

    solveParityGame(pgfile, strategy, outputFile)


###
# Solves the given parity game by using the specified strategy
#
# @param pgfile The file containing the parity game to solve
# @param strategy The strategy to use
# @param outputFile (optional) The file in which to write the output results
###
def solveParityGame(pgfile, strategy, outputFile=None):
    # Initialise and load/parse parity game
    solver = PGSolver()
    solver.loadGame(pgfile)

    # Solve game and output result
    result = solver.solve(strategy)

    # Determine winner of the node at vertex 0, and print
    zeroWinner = "odd"
    if 0 in result['even']:
        zeroWinner = "even"

    output = "The winner of vertex 0 is " + zeroWinner + "\n"
    #output += "Odd nodes: " + str(result['odd']) + "\n"
    #output += "Even nodes: " + str(result['even'])
    print output

    if (outputFile):
        f = open(outputFile, "w")
        f.write(output)
        f.close()
        print "Output written to %s" % outputFile


def printOptions():
    print "Available options:"
    print "   -g, --game <pgfile>: The file containing a parity game in PGSolver format"
    print "   -s, --strategy <input-order|random|predChain|predChainP|predChainS|SCC>: The strategy to use to solve the game."
    print "   -o, --output <file>: write results to given file."
    print "   -h, --help: show available options (this screen)"
    print "   -v, --version: output application version"

# Only execute if not loaded as module!
if __name__ == '__main__':
    run(sys.argv[1:])
