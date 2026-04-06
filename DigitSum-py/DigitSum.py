#!/bin/python3

import math
import os
import random
import re
import sys


def sumedigitos(mm):

    sumatoria = 0

    for e in mm:
        sumatoria += int(e)

    return sumatoria

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# Input x*k
#  1. STRING x
#  2. INTEGER k
#
def superDigit(x):
    #digitos = convertToList(str(x))
    result = 0

    if len(x) <= 1:

        result = int(x)
    else:
        result = sumedigitos(x)

        if result > 9:
            result = superDigit(str(result))

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n*k)

    fptr.write(str(result) + '\n')

    fptr.close()





#print(digisum(9875))
#print(digisum(9875987598759875))
#print(superDigit(str(9875)*4))
#print(superDigit("9875987598759875"*16))
