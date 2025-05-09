#!/bin/python3

import math
import os
import random
import re
import sys

def generate_primes(limit):
    """Generate the first 'limit' prime numbers using the Sieve of Eratosthenes."""
    primes = []
    size = 20000  # Arbitrary upper bound to find 'limit' primes
    sieve = [True] * size
    sieve[0:2] = [False, False]
    
    for num in range(2, size):
        if sieve[num]:
            primes.append(num)
            if len(primes) == limit:
                break
            for multiple in range(num * num, size, num):
                sieve[multiple] = False
    return primes

def waiter(plates, q):
    primes = generate_primes(q)
    answers = []

    for i in range(q):
        prime = primes[i]
        next_stack = []
        current_b = []

        # Process current plates in stack order (LIFO)
        while plates:
            plate = plates.pop()
            if plate % prime == 0:
                current_b.append(plate)
            else:
                next_stack.append(plate)

        # B_i stack goes to answers (top to bottom)
        answers.extend(reversed(current_b))
        plates = next_stack  # A_i becomes input for next round

    # Append any remaining plates (final A stack)
    answers.extend(reversed(plates))
    return answers

if __name__ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()