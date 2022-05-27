firstvalue = int(input('Ingrese un valor: '))
secondvalue = input('Ingrese otro valor: ')

if int(firstvalue) == int(secondvalue):
    print('Los valores son iguales')
    if int(firstvalue) > int(secondvalue):
    print('El primer valor mayor')
    else:
    print('El segundo valor mayor')