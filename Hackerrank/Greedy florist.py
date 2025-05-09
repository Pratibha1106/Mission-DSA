#!/bin/python3

import math
import os
import random
import re
import sys

def getMinimumCost(k, c):
    c = sorted(c, reverse=True) 

    total_cost = 0

    for i in range(len(c)):
        multiplier = (i // k) + 1  
        total_cost += multiplier * c[i]

    return total_cost
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
