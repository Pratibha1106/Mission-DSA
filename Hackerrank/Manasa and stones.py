#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # a_count + b_count = n-1
    answer = []
    if a>b:
        a_count = 0
        b_count = n-1
        while a_count<= n-1:
            tmp = a_count*a+b_count*b
            if tmp not in answer:
                answer.append(tmp)
            a_count+=1
            b_count-=1
    else:
        a_count = n-1
        b_count = 0
        while a_count>= 0:
            tmp = a_count*a+b_count*b
            if tmp not in answer:
                answer.append(tmp)
            a_count-=1
            b_count+=1
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
