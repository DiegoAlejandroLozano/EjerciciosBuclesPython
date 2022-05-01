'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''

num = int(input("Ingrese un número: "))

for i in range(1,11):
    print("%d X %d = %d" % (num, i, (num*i)))