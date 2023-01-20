#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(matriz):
    # Write your code here
    result = None
    
    sumD = 0
    sumI = 0
    tam = len(matriz)-1
    
    for i in range(tam+1):
        sumD += matriz[i][i]
        sumI += matriz[i][tam-i]
        
        
    result = abs(sumD-sumI)
    
    return result




# cada elemento de la lista es una fila
matriz = [[11,2,4],[4,5,6],[10,8,-12]]

print(diagonalDifference(matriz))
