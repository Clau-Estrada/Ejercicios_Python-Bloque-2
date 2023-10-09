'''
Ingresar 10 valores numericos y mostrar cuantos son positivos y cuantos negativos
'''

x = 1
a = 0
b = 0
c = 0
while x <= 10:
    n = int(input(f"Escribe el número {x}: "))
    if n == 0:
        a = a + 1
    else:
        if n < 0:
            b = b + 1
        else:
            c = c + 1
    x += 1

print(f" Estos {a} números son neutros.")
print(f" Estos {b} números son negativos.")
print(f" Estos {c} números son positivos.")
