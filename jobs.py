# Python 3.4.2

import time
import argparse
import operator
from collections import OrderedDict

def main():
    start = time.process_time()

    parser = argparse.ArgumentParser(description='Optimally schedules jobs in decreasing order of the ratio (weight/length).')
    parser.add_argument("-s", help="print the sequence of jobs with corresponding completion times", action="store_true")
    parser.add_argument("-t", help="show execution time", action="store_true")
    parser.add_argument("filename", help=".txt file to parse")
    args = parser.parse_args()
    
    with open(args.filename, 'r') as file:    
            data = file.readlines()

    # list of weight-length pairs
    pairs = [ tuple( map( int, data[i].split() ) ) for i in range(1, len(data)) ]
    # list of weight/length ratios
    ratios = list( map(lambda x: x[0] / x[1],  pairs) )   
    # combined list: [(weight, length), weight/length), ... ]
    combo = list(zip(pairs, ratios))

    # sorting by weight
    initial = sorted(combo, reverse=True)
    # resolving ties: if two jobs have equal ratio, the job with higher weight is scheduled first
    final = sorted(initial, key=operator.itemgetter(1), reverse=True)

    # calculating the sum of weighted completion times
    completionTime = 0
    currentLength = 0
    sequence = OrderedDict()
    for item in final:
        currentLength += item[0][1]
        sequence[item[0]] = currentLength
        completionTime += currentLength * item[0][0]

    print("The sum of weighted completion times: {}".format(completionTime)) 

    if args.s:
        # the order of jobs with completion times: [(weight, length), completion time), ... ]
        finalSequence = [ (key, value) for key, value in sequence.items() ]
        print()
        print("The order of jobs with corresponding completion times: {}".format(finalSequence))

    end = time.process_time()
    if args.t:
        print()
        print("The program ran in {} seconds".format(end - start))

if __name__ == "__main__":
    main()
