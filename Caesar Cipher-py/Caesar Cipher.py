import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, kk):
    result = ""
    isUpp = None
    
    
    abc_a = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"} 
    abc_in = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    
    abc_len = len(abc_in)
    k = kk%abc_len # esto es para cuando KK es muy grande, asi solo calcula las los desplazamientos de k necesarios
    # indice extraido del abc con la letra
    j = None
    # letra extraido del abc con la letra
    l= " "
    
    i = 0
    while i < len(s):
        
        isUpp = s[i].isupper()
        
        if s[i].lower() in abc_in.keys():
            j = abc_in[s[i].lower()]
            
            if j+k > abc_len:
                l = abc_a[(j+k)%abc_len] #aca tener en cuenta el residuo para ajustar la rotacion
            else:
                l = abc_a[j+k]
            
            if isUpp:
                l = l.upper()
                
            result+=l
        else:
            result+=s[i]
        
        j=None
        l = None
        isUpp = None
        i+=1
    return result

print(caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 26))
print(caesarCipher("middle-Outz",2))  
print(caesarCipher("A/b*wXy%Z",3))    
print(caesarCipher("There's-a-starman-waiting-in-the-sky",3))
print(caesarCipher("There's-a-starman-waiting-in-the-sky",100))
print(caesarCipher("Always-Look-on-the-Bright-Side-of-Life", 100))




def creardicc(s):
    result2 = "{" 
    result1 = "{"
    for i in range(len(s)):
        result1 += '{}: "{}", '.format(i+1, s[i])
        result2 += '"{}": {}, '.format(s[i],i+1)
    result1 += "}"
    result2 += "}"
    return result1, result2
    
#print(creardicc("abcdefghijklmnopqrstuvwxyz"))