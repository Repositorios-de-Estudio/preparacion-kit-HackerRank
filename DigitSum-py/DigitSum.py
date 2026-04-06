


def convertToList(y):
    ss = str(y)
    nums = []

    for e in ss:
        nums.append(int(e))
    return nums


def sumedigitos(mm):
    sumatoria = 0

    for e in mm:
        sumatoria += e

    return sumatoria

def digisum(x):
    digitos = convertToList(x)
    result = 0

    if len(digitos) < 2:
        result = digitos[0]
    else:
        result = sumedigitos(digitos)

        if result > 9:
            result = digisum(result)

    return result




#print(digisum(9875))
print(digisum(9875987598759875))
