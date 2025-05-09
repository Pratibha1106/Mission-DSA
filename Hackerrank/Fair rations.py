#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    count=0
    # Write your code here
    def isEvens(arr):
        for i in arr:
            if i%2 != 0:
                return False
        return True
    for j in range(len(B)):
        if B[j] % 2 != 0:
            if j == len(B)-1:
                return 'NO'
            B[j]+=1
            B[j+1]+=1
            count+=2
            if isEvens(B):
                return str(count)
    return '0'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
