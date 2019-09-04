#!/bin/python3
# 12
# DDUUDDUDUUUD
# o/p : 2 valleys.
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sum = 0
    valley = 0
    for i in s:
        if i == 'U':
            sum += 1
        else:
            sum -= 1
        if sum == 0 and i == 'U':
            valley += 1
    return valley                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
