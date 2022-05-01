'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''

num = int(input("Ingrese un número entero: "))

if (num%2)==0:
    print("Es un número primo")
else:
    print("No es un número primo")