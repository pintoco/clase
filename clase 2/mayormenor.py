firstvalue = int(input('Ingrese primer valor: '))
secondvalue = int(input('Ingrese segundo valor: '))
thirdvalue = int(input('ingrese tercer valor: '))

if firstvalue < secondvalue:
    aux = firstvalue
    firstvalue = secondvalue
    secondvalue = aux
if secondvalue < thirdvalue:
    aux = secondvalue
    secondvalue = thirdvalue
    thirdvalue = aux
if firstvalue < secondvalue:
    aux = firstvalue
    firstvalue = secondvalue
    secondvalue = aux
print ('Los valores ordenados de menor a mayor son: ')
print(firstvalue, '-',secondvalue, '-',thirdvalue)