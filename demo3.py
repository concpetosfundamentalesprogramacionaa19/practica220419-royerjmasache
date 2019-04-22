"""
	archivo: demo3.py
	Ingreso de datos desde teclado
	autor: royerjmasache
"""
import sys
# Ingreso de datos
valor1 = input("Ingrese el valor del primer número: ")
valor2 = input("Ingrese el valor del segundo número: ")
# Se realizan las operaciones y se la almacenan en las variables
suma = int(valor1) + int(valor2)
producto = int(valor1) * int(valor2)
# Presentación de datos
print ("El resultado de la suma es de: %d\nEl restultado de la multiplicación es: %d" % (suma, producto))
