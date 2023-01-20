


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

#from ast import Dict


def lonelyinteger(lista):
    # Write your code here
    
    result = None
    
    ddd = dict()
    
    for num in lista:
        if not(num in ddd.keys()):
            ddd[num]=1
        elif num in ddd.keys():
            ddd[num]+=1
            
    for x in ddd.keys():
        if ddd[x]==1:
            result = x        
            break
    return result




lista = [4,1,2,3,5,5,3,2,1,4,0]


print(lonelyinteger(lista))
