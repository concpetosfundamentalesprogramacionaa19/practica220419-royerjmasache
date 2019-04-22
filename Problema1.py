"""
	Archivo: Problema1.py
	Problema 1 del taller de laboratorio
	autor: royejmasache
"""
import sys
# Ingreso de datos
numHoras = input("Ingrese el número de horas: ")
costo = input("Ingrese el costo por hora oficial: ")
# Se calcula el suelto total y se almacena en la variable
sueldot = float(numHoras) * float(costo)
# Se calcula el descuento y se almacena en la variable
descuento = float(sueldot) * 0.1
# Se calcula el sueldo real y se almacena en la variable
sueldo = float(sueldot) - float(descuento)
# Se preseta el resultado
print("El descuento realizado es de: %.1f\nEl sueldo mensual del trabajador es de: %.1f" % (descuento, sueldo))
	