#!/usr/bin/python2

# Randomly sample line from the input files listed as arguments
# Skip first line and sample with probability 1/20

import sys
import random

def sample_file(file):
    with open(file, 'r') as fin:
        next(fin)
        for line in fin:
            if (random.randint(1,20) == 20):
                print line,

for i in sys.argv[1:]:
    sample_file(i)


