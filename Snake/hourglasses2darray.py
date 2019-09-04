#!/bin/python3
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# o/p = 19
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    k,l = 1,1 
    maxno = arr[k-1][l-1] + arr[k-1][l] + arr[k-1][l+1] +arr[k][l] +arr[k+1][l-1] +arr[k+1][l] +arr[k+1][l+1] 
    for i in range(1,5):
        for j in range(1,5):
            maxn = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] +arr[i][j] +arr[i+1][j-1] +arr[i+1][j] +arr[i+1][j+1]
            if maxn > maxno :
                maxno = maxn
    return maxno

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
