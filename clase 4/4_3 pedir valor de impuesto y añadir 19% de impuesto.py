# 32000 valor original, 19 es porcentaje de aumento
aumento = (32000 * 19)/100    # Regla de 3 de álgebra

def sumTwoValues(valorOriginal: int, aumento: int):
    localSum = int(valorOriginal + aumento)
    return localSum

print(sumTwoValues(32000, aumento))


# Pero la manera correcta de hacerlo es:

def taxesCacl(userValue: int):
    tax = userValue * 0.19
    return userValue + tax

firstValue = int(input('Ingrese un valor: '))
print('El valor de el impuesto en total es:', taxesCacl(firstValue))