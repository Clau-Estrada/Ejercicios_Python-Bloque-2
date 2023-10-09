'''
Tomando la fecha de nacimiento ingresada por la usuario, calcular el número de días que ha vivido.
1. Importar módulo datetime.
2. Imprimir lo que se hará.
3. Crear tres variables con int para que ingresen, día, mes y año.
4. Crear variable fecha actual (al primero de enero).
5. Crear variable fecha nacimiento con función date y modulo datetime.
6. Crear variable que reste fecha actual de fecha de nac.
7. Imprimir días transcurridos, pero con .days.
'''
import datetime

print("A continuación se calcularán los días transcurridos desde tu fecha de nacimiento.")
dia = int(input("Introduce el día de tu nacimiento: "))
mes = int(input("Ahora el mes en número, ej. abril = 4: "))
anio = int(input("Por último el año: "))

fecha_actual = datetime.date(2023, 1, 1)
fecha_nacimiento = datetime.date(anio, mes, dia)

result = fecha_actual - fecha_nacimiento

print(f"Los días transcurridos son {result.days} aproximadamente.")
