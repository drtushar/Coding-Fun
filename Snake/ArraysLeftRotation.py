#!/bin/python3
# 5 4
# 1 2 3 4 5
# Expected OutputDownload
# 5 1 2 3 4
import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a,n,d):
    result = list(range(n))
    for i in range(n):
        result[(n-d+i)%n] = a[i]
    return result            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a,n,d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
