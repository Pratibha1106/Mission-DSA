#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    mod = 10**9 + 7
    digits = list(map(int, n))
    N = len(n)

    fn = digits[0]
    dfn = fn

    for i in range(1, N):
        current_digit = digits[i]

        dfn = (10 * dfn + (i + 1) * current_digit) % mod
        fn = (fn + dfn) % mod

    return fn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
