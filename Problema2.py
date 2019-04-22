"""
	Archivo: Problema2.py
	Problema 2 del taller de laboratorio
	autor: royerjmasache
"""
# Ingreso de datos
x = input("Ingrese el valor de la variable x: ")
y = input("Ingrese el valor de la variable y: ")
z = input("Ingrese el valor de la variable z: ")
# Se realiza la operación y se almacena en la variable
m = ((float(x) + float(y)/float(z))/(float(x) - float(y)/float(z)))
# Se presenta el resultado
print("El valor de m en base a las variables:\nx = %.1f\n\ty = %.1f\n\t\tz = %.1f\nda como resultado:\n\t\t m = %.1f" % (float(x), float(y), float(z), m))
