'''
Calcular el incremento salarial de una persona. 
Si su salario es menor a 15mil el incremento será del 20% y si es mayor a 15mil el incremento será del 15%
'''

salario = int(input("Captura el salario actual del trabajador: "))

if salario <= 15000:
    salario += (salario * 0.20)
    print("El nuevo salario del profesor es", salario)
else:
    salario += (salario * 0.15)
    print("El nuevo salario del profesor es", salario)
