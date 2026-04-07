#!/bin/python3

import math
import os
import random
import re
import sys


def sumedigitos(mm, kk):

    sumatoria = 0

    for e in mm:
        sumatoria += int(e)

    return sumatoria*kk

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# Input x*k
#  1. STRING x
#  2. INTEGER k
#
def superDigit(x, k):
    #digitos = convertToList(str(x))
    result = 0

    if len(x) <= 1:

        result = int(x)
    else:
        result = sumedigitos(x, k)

        if result > 9:
            result = superDigit(str(result), 1)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



####
#alguna forma de hacer la sum(x)*k, parece evitar hacer la sum(x*k) que es mucho mas grande
# por eso multiplico la suma de x por k en sumedigitos() en vez de calcular la suma de x*k, porque
# sum(x*k)=sum(x)*k, y este ultimo es mucho mas rapido de calcular al ser una multiplicacion de enteros


#print(superDigit(str(9875)*4))
#print(superDigit("9875987598759875"*16))
