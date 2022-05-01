'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el 
capital obtenido en la inversión cada año que dura la inversión.
'''

cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual: "))
años = int(input("Ingrese el número de años: "))

porcentaje_ganancia = None

for i in range(años):
    porcentaje_ganancia = (interes_anual/100) * cantidad_invertir
    cantidad_invertir = cantidad_invertir + porcentaje_ganancia

    print("Capital obtenido: %.2f\tAño: %d" % (cantidad_invertir, (i+1)))
