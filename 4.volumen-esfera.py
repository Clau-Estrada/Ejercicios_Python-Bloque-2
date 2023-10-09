'''
Calcular el volumen de una esfera
1. Crear variable con float para que ingrese los datos del radio.
2. Agregar valor de pi.
3. Crear nueva variavle con la operación aritmética.
4. Imprimir el resultado de volumen en metro cúbico.
'''
radio = float(input("Escribe el valor del radio: "))
valor_pi = 3.1416
volumen = 4 / 3 * valor_pi * (radio * radio * radio)
print(f"{volumen} m³")
