
#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
# SOLUCION TOMADA DE LA WIKI
def towerBreakers(n, m):
    ganador = 0
    if m == 1: 
        ganador=2
    else:
        if n % 2 == 1:
            ganador=1
        else:
            ganador=2
    return ganador    
        
print(towerBreakers(2,6)) #2
print(towerBreakers(2,2)) #2           
print(towerBreakers(1,4)) #1