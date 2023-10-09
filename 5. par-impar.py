'''
Ingresar 10 valores numéricos y mostrar cuántos son pares y cuantos impares.
'''
x = 1
par = impar = 0
while x <= 10:
    n = int(input(f"Ingresa un número {x}: "))
    if n > 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    x += 1
print("El total de números pares es: ", par)
print("El total de números impares es: ", impar)
