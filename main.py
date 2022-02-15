# OpenBootcamp Curso Python Ejercicio 5

#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra
# función que calcule el área de un círculo recibiendo el radio del mismo.

def calcularAreaTriangulo(altura, base):
    return base * altura / 2

def calcularAreaCirculo(radio):
    pi = 3.14159
    return pi * (radio * radio)

print(calcularAreaTriangulo(5, 4))
print(calcularAreaCirculo(5))
