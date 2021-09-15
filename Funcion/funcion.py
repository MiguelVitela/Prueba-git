import math
def sumar(a, b):
    suma = a + b
    return suma

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
resultado = sumar(numero1, numero2)

print("La suma de {} y {} es igual a {}".format(numero1, numero2, resultado))

# Muestra el valor de la constante de Euler
print(math.e)
print(math.sin(56))
print(math.sin(math.pi))
print(math.tan(math.pi))
print(math.cos(math.pi))