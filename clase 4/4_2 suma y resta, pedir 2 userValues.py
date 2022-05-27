
def sumTwoValues(oneValue: int, twoValue: int):
    localSum = oneValue + twoValue
    return localSum

def subTwoValues(oneValue: int, twoValue: int):
    localSub = oneValue - twoValue
    return localSub

oneValue = int(input('Ingrese un valor: '))
twoValue = int(input('Ingrese otro valor: '))

print('El resultado de la suma es: ', sumTwoValues(oneValue, twoValue))

print('El resultado de la resta es: ', subTwoValues(oneValue, twoValue))