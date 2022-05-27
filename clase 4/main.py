def helloMessage(firstName):     # def = definir una función   # <----- esta linea espara un nombre de la línea 4, aqui es solo la deficnicion, no espera input
    print('Hello', firstName, '!!!')    # este bloque define helloMessage, () lo marca como función y def lo *da una definición a la función*
    
helloMessage('Maria')         # linea donde se le da nombre a la función para la definicion de linea 1?
helloMessage('Luis')
helloMessage('Marco')
helloMessage('Frescia')
    
    
def sumTwoValues(oneValue: int, twoValue: int):
    localSum = oneValue + twoValue
    return localSum                     # return es una función que retorna(?) el resultado de una función, no solo la presenta (retornar es mandar el resultado a algún lugar, línea o definicion)
    
result = sumTwoValues(5, 4)             # result es una función para simplemente postrar el resultado de una variable
print(result)

# o también

print(sumTwoValues(5,3))
    