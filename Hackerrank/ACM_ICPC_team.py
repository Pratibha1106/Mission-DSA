#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    int_masks = [int(topic_i, 2) for topic_i in topic] # convert to integers from binary string

    known_topics = 0
    known_topics_people = 0

    for i in range(len(topic)):
        for j in range(i +1, len(topic)): #we start iterating from a new i !!
            overlap = bin(int_masks[i] | int_masks[j]).count("1")
            if overlap > known_topics:
                known_topics = overlap
                known_topics_people = 1
            elif overlap == known_topics:
                known_topics_people += 1
            
    return known_topics, known_topics_people
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
