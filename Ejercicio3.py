'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

numero = int(input("Ingrese un número entero positivo: "))

for i in range(numero):

    iterador = i+1

    if (iterador%2) != 0:
        print(iterador, end=', ')