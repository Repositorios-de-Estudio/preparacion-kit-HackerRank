#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#



# SOLUCION TOMADA DEL FORO
def flippingMatrix2(matrix):
    
    midd = len(matrix)//2
    tam = len(matrix)-1
    suma = 0
    maximo = 0
    
    for i in range(midd):
        for j in range(midd):
            
            #print("blucle: ") 
            
            #print(matrix[i][j], i, j )
            #print(matrix[i][tam-j],i, tam-j )
            #print(matrix[tam-i][j], tam-i, j )
            #print(matrix[tam-i][tam-j], tam-i, tam-j )
            
            #print("fin: ")
            #               estas son las 4 esquinas de la matriz
            #               el for evalua 4 submatrices: toda, centra
            #               se busca evualar todos los valores 
            maximo =  max(matrix[i][j],matrix[i][tam-j],matrix[tam-i][j],matrix[tam-i][tam-j])
            print(maximo)
            suma+= maximo
            
    return suma






# matriz = [[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]
matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


print(flippingMatrix2(matriz))