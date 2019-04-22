"""
	archivo: demo2.py
	Multiplicación en lenguaje Python
	autor: royerjmasache
"""
import  sys
nombreArchivo = sys.argv[0]
valor1 = sys.argv[1]
valor2 = sys.argv[2]
# En la siguiente variable se almacena la suma
suma = int(valor1) + int(valor2)
print("La suma es: %d" % suma)